import sys

class Team(object):
    """docstring for Team."""
    def __init__(self, rank, name, wins, losses, otl, points):
        super(Team, self).__init__()
        self.rank = rank
        self.name = name
        self.wins = wins
        self.losses = losses
        self.otl = otl
        self.points = points

teamNameDict = {'ANAHEIM':'ANAHEIM DUCKS',
                'DUCKS':'ANAHEIM DUCKS',
                'ANAHEIM DUCKS':'ANAHEIM DUCKS',
                'ANA':'ANAHEIM DUCKS',
                'ARIZONA':'ARIZONA COYOTES',
                'COYOTES':'ARIZONA COYOTES',
                'ARIZONA COYOTES':'ARIZONA COYOTES',
                'YOTES':'ARIZONA COYOTES',
                'ARI':'ARIZONA COYOTES',
                'BOSTON':'BOSTON BRUINS',
                'BRUINS':'BOSTON BRUINS',
                'BOSTON BRUINS':'BOSTON BRUINS',
                'BOS':'BOSTON BRUINS',
                'BUFFALO':'BUFFALO SABRES',
                'SABRES':'BUFFALO SABRES',
                'BUF':'BUFFALO SABRES',
                'CALGARY':'CALGARY FLAMES',
                'FLAMES':'CALGARY FLAMES',
                'CALGARY FLAMES':'CALGARY FLAMES',
                'CGY':'CALGARY FLAMES',
                'CAROLINA':'CAROLINA HURRICANES',
                'HURRICANES':'CAROLINA HURRICANES',
                'CAROLINA HURRICANES':'CAROLINA HURRICANES',
                'CANES':'CAROLINA HURRICANES',
                'CAR':'CAROLINA HURRICANES',
                'CHICAGO':'CHICAGO BLACKHAWKS',
                'BLACKHAWKS':'CHICAGO BLACKHAWKS',
                'CHICAGO BLACKHAWKS':'CHICAGO BLACKHAWKS',
                'HAWKS':'CHICAGO BLACKHAWKS',
                'CHI':'CHICAGO BLACKHAWKS',
                'COLORADO':'COLORADO AVALANCHE',
                'AVALANCHE':'COLORADO AVALANCHE',
                'COLORADO AVALANCHE':'COLORADO AVALANCHE',
                'AVS':'COLORADO AVALANCHE',
                'COL':'COLORADO AVALANCHE',
                'COLUMBUS':'COLUMBUS BLUE JACKETS',
                'BLUE JACKETS':'COLUMBUS BLUE JACKETS',
                'JACKETS':'COLUMBUS BLUE JACKETS',
                'COLUMBUS BLUE JACKETS':'COLUMBUS BLUE JACKETS',
                'CBJ':'COLUMBUS BLUE JACKETS',
                'DALLAS':'DALLAS STARS',
                'STARS':'DALLAS STARS',
                'DALLAS STARS':'DALLAS STARS',
                'DAL':'DALLAS STARS',
                'DETROIT':'DETROIT RED WINGS',
                'RED WINGS':'DETROIT RED WINGS',
                'WINGS':'DETROIT RED WINGS',
                'DETROIT RED WINGS':'DETROIT RED WINGS',
                'DET':'DETROIT RED WINGS',
                'EDMONTON':'EDMONTON OILERS',
                'OILERS':'EDMONTON OILERS',
                'EDMONTON OILERS':'EDMONTON OILERS',
                'EDM':'EDMONTON OILERS',
                'FLORIDA':'FLORIDA PANTHERS',
                'PANTHERS':'FLORIDA PANTHERS',
                'FLORIDA PANTHERS':'FLORIDA PANTHERS',
                'CATS':'FLORIDA PANTHERS',
                'FLA':'FLORIDA PANTHERS',
                'LOS ANGELES':'LOS ANGELES KINGS',
                'KINGS':'LOS ANGELES KINGS',
                'LOS ANGELES KINGS':'LOS ANGELES KINGS',
                'LA':'LOS ANGELES KINGS',
                'L.A':'LOS ANGELES KINGS',
                'L.A.':'LOS ANGELES KINGS',
                'LAK':'LOS ANGELES KINGS',
                'MINNESOTA':'MINNESOTA WILD',
                'WILD':'MINNESOTA WILD',
                'MINNESOTA WILD':'MINNESOTA WILD',
                'MIN':'MINNESOTA WILD',
                'MONTREAL':'MONTREAL CANADIENS',
                'CANADIENS':'MONTREAL CANADIENS',
                'MONTREAL CANADIENS':'MONTREAL CANADIENS',
                'HABS':'MONTREAL CANADIENS',
                'MTL':'MONTREAL CANADIENS',
                'NASHVILLE':'NASHVILLE PREDATORS',
                'PREDATORS':'NASHVILLE PREDATORS',
                'NASHVILLE PREDATORS':'NASHVILLE PREDATORS',
                'PREDS':'NASHVILLE PREDATORS',
                'NSH':'NASHVILLE PREDATORS',
                'NEW JERSEY':'NEW JERSEY DEVILS',
                'JERSEY':'NEW JERSEY DEVILS',
                'DEVILS':'NEW JERSEY DEVILS',
                'NEW JERSEY DEVILS':'NEW JERSEY DEVILS',
                'NJD':'NEW JERSEY DEVILS',
                'ISLANDERS':'NEW YORK ISLANDERS',
                'NEW YORK ISLANDERS':'NEW YORK ISLANDERS',
                'ISLES':'NEW YORK ISLANDERS',
                'NYI':'NEW YORK ISLANDERS',
                'RANGERS':'NEW YORK RANGERS',
                'NEW YORK RANGERS':'NEW YORK ISLANDERS',
                'NYR':'NEW YORK ISLANDERS',
                'OTTAWA':'OTTAWA SENATORS',
                'SENATORS':'OTTAWA SENATORS',
                'OTTAWA SENATORS':'OTTAWA SENATORS',
                'SENS':'OTTAWA SENATORS',
                'OTT':'OTTAWA SENATORS',
                'PHILADELPHIA':'PHILADELPHIA FLYERS',
                'FLYERS':'PHILADELPHIA FLYERS',
                'PHILADELPHIA FLYERS':'PHILADELPHIA FLYERS',
                'PHILLY':'PHILADELPHIA FLYERS',
                'PHI':'PHILADELPHIA FLYERS',
                'PITTSBURGH':'PITTSBURGH PENGUINS',
                'PENGUINS':'PITTSBURGH PENGUINS',
                'PITTSBURGH PENGUINS':'PITTSBURGH PENGUINS',
                'PENS':'PITTSBURGH PENGUINS',
                'PIT':'PITTSBURGH PENGUINS',
                'SAN JOSE':'SAN JOSE SHARKS',
                'SHARKS':'SAN JOSE SHARKS',
                'SAN JOSE SHARKS':'SAN JOSE SHARKS',
                'SHARKIES':'SAN JOSE SHARKS',
                'SJS':'SAN JOSE SHARKS',
                'ST LOUIS':'ST. LOUIS BLUES',
                'ST. LOUIS':'ST. LOUIS BLUES',
                'BLUES':'ST. LOUIS BLUES',
                'ST LOUIS BLUES':'ST. LOUIS BLUES',
                'ST. LOUIS BLUES':'ST. LOUIS BLUES',
                'STL':'ST. LOUIS BLUES',
                'TAMPA':'TAMPA BAY LIGHTNING',
                'TAMPA BAY':'TAMPA BAY LIGHTNING',
                'LIGHTNING':'TAMPA BAY LIGHTNING',
                'TAMPA BAY LIGHTNING':'TAMPA BAY LIGHTNING',
                'BOLTS':'TAMPA BAY LIGHTNING',
                'TBL':'TAMPA BAY LIGHTNING',
                'TORONTO':'TORONTO MAPLE LEAFS',
                'MAPLE LEAFS':'TORONTO MAPLE LEAFS',
                'LEAFS':'TORONTO MAPLE LEAFS',
                'TORONTO MAPLE LEAFS':'TORONTO MAPLE LEAFS',
                'BUDS':'TORONTO MAPLE LEAFS',
                'TML':'TORONTO MAPLE LEAFS',
                'TOR':'TORONTO MAPLE LEAFS',
                'VANCOUVER':'VANCOUVER CANUCKS',
                'CANUCKS':'VANCOUVER CANUCKS',
                'VANCOUVER CANUCKS':'VANCOUVER CANUCKS',
                'NUCKS':'VANCOUVER CANUCKS',
                'VAN':'VANCOUVER CANUCKS',
                'VEGAS':'VEGAS GOLDEN KNIGHTS',
                'KNIGHTS':'VEGAS GOLDEN KNIGHTS',
                'VEGAS GOLDEN KNIGHTS':'VEGAS GOLDEN KNIGHTS',
                'VGK':'VEGAS GOLDEN KNIGHTS',
                'WASHINGTON':'WASHINGTON CAPITALS',
                'CAPITALS':'WASHINGTON CAPITALS',
                'WASHINGTON CAPITALS':'WASHINGTON CAPITALS',
                'CAPS':'WASHINGTON CAPITALS',
                'WSH':'WASHINGTON CAPITALS',
                'WINNIPEG':'WINNIPEG JETS',
                'JETS':'WINNIPEG JETS',
                'WINNIPEG JETS':'WINNIPEG JETS',
                'WPG':'WINNIPEG JETS'
               }

def breakdownRecord(record):
    values = record.split('-')
    wins = int(values[0])
    losses = int(values[1])
    otl = int(values[2])
    points = wins * 2 + otl
    return wins,losses,otl,points

def main():
    #bring in current team names and standings and create list of teams
    teamList = []
    standings = open('currentStandings.csv','r')

    #reads teams into teamList for use later
    for line in standings:
        values = line.split(',')
        wins,losses,otl,points = breakdownRecord(values[2])
        newTeam = Team(values[0],values[1],wins,losses,otl,points)
        teamList.append(newTeam)

    if len(sys.argv) == 1 or len(sys.argv) > 4:
        print('Usage: ../PlayoffHope.py TEAMNAME')
    else:
        #get name of team entered and make sure it matches a team in the list
        if len(sys.argv) == 2:
            break
        elif len(sys.argv) == 3:
            break
        elif len(sys.argv) == 4:
            break

if __name__ == '__main__':
    main()
