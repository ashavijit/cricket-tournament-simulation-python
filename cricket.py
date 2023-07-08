import random

class Player:
    def __init__(self, name, batting, bowling, fielding, running, experience):
        self.name = name
        self.batting = batting
        self.bowling = bowling
        self.fielding = fielding
        self.running = running
        self.experience = experience

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []

    def select_captain(self, player):
        self.captain = player

    def send_next_player(self):
        if len(self.batting_order) < len(self.players):
            player = self.players[len(self.batting_order)]
            self.batting_order.append(player)
            return player
        else:
            return None

    def choose_bowler(self):
        return random.choice(self.players)

class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

class Umpire:
    def __init__(self, field):
        self.field = field
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def play_ball(self, batsman, bowler):
        if random.random() < batsman.batting:
            self.score += 1
            print("{} scores 1 run.".format(batsman.name))

        else:
            self.wickets += 1
            print("{} is out!".format(batsman.name))
            self.batting_order.remove(batsman)

    def play_over(self, batting_team, bowling_team):
        print("New over begins!")
        bowler = bowling_team.choose_bowler()
        for _ in range(6):
            batsman = batting_team.send_next_player()
            if batsman is None:
                break
            self.play_ball(batsman, bowler)
        self.overs += 1

class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def comment(self):
        print("Score: {}-{} in {} overs.".format(self.umpire.score, self.umpire.wickets, self.umpire.overs))

# Example usage
player1 = Player("MS Dhoni", 0.8, 0.2, 0.99, 0.8, 0.9)
player2 = Player("Virat Kohli", 0.9, 0.1, 0.95, 0.7, 0.8)
player3 = Player("Rohit Sharma", 0.85, 0.1, 0.9, 0.75, 0.85)

team1 = Team("Team 1", [player1, player2, player3])
team1.select_captain(player1)

team2 = Team("Team 2", [player1, player2, player3])
team2.select_captain(player2)

field = Field("Large", 0.8, "Dry", 0.1)

umpire = Umpire(field)
commentator = Commentator(umpire)

umpire.play_over(team1, team2)
commentator.comment()
