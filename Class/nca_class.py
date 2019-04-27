# 64 - 16 teams - 4 region - seats 1 to 16

# name of region - string
# list of teams still remaining
# number of games played - int
class region() :

    def __init__(self, name, teams) :
        self.name = name
        self.teams = teams
        self.games_played = 0

    def eliminiation(self, name) :
        self.teams.remove(name)

    def play_game(self) :
        self.games_played += 1
