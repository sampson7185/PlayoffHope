from PlayoffHopeDicts import *
import sys
from operator import itemgetter, attrgetter

class Team(object):
    """docstring for Team."""
    def __init__(self, name, wins, losses, otl, points, played):
        super(Team, self).__init__()
        self.name = name
        self.wins = wins
        self.losses = losses
        self.otl = otl
        self.points = points
        self.gamesPlayed = played

    def __repr__(self):
        return '{},{},{},{},{},{}'.format(self.name,
                                  self.gamesPlayed,
                                  self.wins,
                                  self.losses,
                                  self.otl,
                                  self.points)

targetTeamName = ''
targetTeamDiv = ''
targetOtherDiv = ''
targetTeamConf = ''

def getPos(team):
    return team[1]

def breakdownRecord(record):
    values = record.split('-')
    wins = int(values[0])
    losses = int(values[1])
    otl = int(values[2])
    points = wins * 2 + otl
    played = wins + losses + otl
    return wins,losses,otl,points,played

def getTeamName(name):
    global targetTeamName
    #capitalize name
    capitalized = name.upper()
    try:
        targetTeamName = teamNameDict[capitalized]
    except KeyError as e:
        return False

    return True

#Result Enum:
#   1: Home team wins in regulation
#   2: Away team wins in regulation
#   3: Home team wins in overtime/shootout
#   4: Away team wins in overtime/shootout
def updateStats(teamList,homeTeam,awayTeam,result):
    for team in teamList:
        if team.name == (homeTeam.upper()).rstrip():
            team.gamesPlayed = team.gamesPlayed + 1
            if result == 1 or result == 3:
                team.wins = team.wins + 1
                team.points = team.points + 2
            elif result == 2:
                team.losses = team.losses + 1
            elif result == 4:
                team.otl = team.otl + 1
                team.points = team.points + 1
        elif team.name == (awayTeam.upper()).rstrip():
            team.gamesPlayed = team.gamesPlayed + 1
            if result == 2 or result == 4:
                team.wins = team.wins + 1
                team.points = team.points + 2
            elif result == 1:
                team.losses = team.losses + 1
            elif result == 3:
                team.otl = team.otl + 1
                team.points = team.points + 1

def simulateRemainingGames(teamList):
    #open remianing schedule
    remainingSched = open('remainingGames.csv','r')

    for line in remainingSched:
        values = line.split(',')
        updateStats(teamList,values[2],values[1],1)

def printStandings(teamList,toFile):
    if toFile:
        standings = open('standingsOutput.csv','w')
        standings.write('Team,Games Played,Wins,Losses,OTL,Points\n')
    else:
        print ('Team, Games Played, Wins, Losses, OTL, Points')

    for team in sorted(teamList,key=attrgetter('points'),reverse=True):
        if toFile:
            standings.write(repr(team) + "\n")
        else:
            print (team)

#returns true if team x beats team y, false if y beats x
def checkTeamAhead(teamx, teamy):
    if teamx.points > teamy.points:
        return True
    elif teamx.points < teamy.points:
        return False
    elif teamx.points == teamy.points:
        if teamx.wins > teamy.wins:
            return True
        elif teamx.wins < teamy.wins:
            return False

#This checks position of desired team vs rest of teams (typically a division).
#TODO: In case of ties, this compares wins, but some more criteria if still tie
#which should be added to this check, tie breakers listed below in order of precedence
#1. Most wins
#2. Most points in games against each other among the tied teams
#3. The greater positive differential between goals scored for and against among the tied teams.
def getTeamPos(teamList,targetTeam):
    teamPos = 1
    for team in teamList:
        if targetTeam.name == targetTeamName and team.name == targetTeamName:
            continue
        elif checkTeamAhead(team,targetTeam):
            teamPos = teamPos + 1

    return teamPos

def checkTargetTeamViability(targetTeam,teamList):
    canMakeFirst = False
    canMakeSecond = False
    canMakeThird = False
    #Find which spots are possible to reach if any
    for team in teamList:
        #if target team wins all games, can they pass the top 3 in the division?
        if (targetTeam.points + ((82 - targetTeam.gamesPlayed)*2) > team[0].points or
            (targetTeam.points + ((82 - targetTeam.gamesPlayed)*2) == team[0].points and
            targetTeam.wins + (82 - targetTeam.gamesPlayed) > team[0].wins)):
            if (team[1] == 1):
                canMakeFirst = True
            if (team[1] == 2):
                canMakeSecond = True
            if (team[1] == 3):
                canMakeThird = True

    return canMakeFirst, canMakeSecond, canMakeThird

def getPossiblePlayoffPos(teamList):
    canMakeFirst = False
    canMakeSecond = False
    canMakeThird = False
    sameDivisionCount = 0
    otherDivisionCount = 0
    #create a list of all teams in same division
    sameDivision = []
    #create a list of all teams in same conference
    sameConf = []
    #create a list of two current wildcard teams
    currentWC = []
    #create a list of tuples (team, divisionalPosition)
    teamWithDivPos = []
    #create a list of tuples (team, confPosition)
    teamWithConfPos = []
    for team in teamList:
        if (targetTeamDiv == divDict[team.name]):
            sameDivision.append(team)
        if (targetTeamName == team.name):
            targetTeam = team
        if (targetTeamConf == confDict[team.name]):
            sameConf.append(team)

    for team in sameDivision:
        teamWithDivPos.append((team,getTeamPos(sameDivision,team)))

    for team in sameConf:
        teamWithConfPos.append((team,getTeamPos(sameConf,team)))

    #Find which wildcard spots are possible to reach if any
    #NOTE:Related to note about div positions, this will also need to have the more
    #subtle rules added to it once it is more complete, for now will just use wins
    #as a tie breaker
    #go through the conference standings and get top three from target division and other
    #conference division and then take top 2 left over as wildcard
    for team in sorted(teamWithConfPos,key=getPos):
        #check if any div spots are available
        if divDict[team[0].name] == targetTeamDiv and sameDivisionCount < 3:
            sameDivisionCount = sameDivisionCount + 1
        elif divDict[team[0].name] == targetOtherDiv and otherDivisionCount < 3:
            otherDivisionCount = otherDivisionCount + 1
        else:
            if len(currentWC) == 0:
                currentWC.append((team[0],1))
            elif len(currentWC) == 1:
                currentWC.append((team[0],2))
            else:
                break

    #Find which divisional spots are possible to reach if any
    canMakeFirst, canMakeSecond, canMakeThird = checkTargetTeamViability(targetTeam,teamWithDivPos)

    #check if team can make current WC positions
    canMakeWC1, canMakeWC2, garbage = checkTargetTeamViability(targetTeam,currentWC)

def main():
    global targetTeamDiv, targetTeamConf, targetOtherDiv
    #bring in current team names and standings and create list of teams
    teamList = []
    standings = open('currentStandings.csv','r')

    #reads teams into teamList for use later
    for line in standings:
        values = line.split(',')
        wins,losses,otl,points,played = breakdownRecord(values[2])
        newTeam = Team(values[1].upper(),wins,losses,otl,points,played)
        teamList.append(newTeam)

    if len(sys.argv) == 1 or len(sys.argv) > 4:
        print('Usage: ../PlayoffHope.py TEAMNAME')
    else:
        #get name of team entered and make sure it matches a team in the list
        if len(sys.argv) == 2:
            foundTeam = getTeamName(sys.argv[1])
        elif len(sys.argv) == 3:
            foundTeam = getTeamName(sys.argv[1] + ' ' + sys.argv[2])
        elif len(sys.argv) == 4:
            foundTeam = getTeamName(sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3])

        if foundTeam:
            print ("Team found, simulating remaining games...")
            targetTeamDiv = divDict[targetTeamName]
            targetOtherDiv = otherDivDict[targetTeamDiv]
            targetTeamConf = confDict[targetTeamName]
            #based on division and current standing, figure out what positions are possible
            getPossiblePlayoffPos(teamList)
            simulateRemainingGames(teamList)
            printStandings(teamList,True)

if __name__ == '__main__':
    main()
