class Player:
    def __init__(self, name, exactResult, winningIdentity, points, homeBet, awayBet):
        self.name = name
        self.exactResult = exactResult
        self.winningIdentity = winningIdentity
        self.points = points
        self.homeBet = homeBet
        self.awayBet = awayBet

    # Getters:

    def get_name(self):
        return self.name

    def get_exact_result(self):
        return self.exactResult

    def get_winning_identity(self):
        return self.winningIdentity

    def get_points(self):
        return self.points

    def get_home_bet(self):
        return self.homeBet

    def get_away_bet(self):
        return self.awayBet

    # Setters:

    def set_exact_result(self, value):
        self.exactResult = value

    def set_winning_identity(self, value):
        self.winningIdentity = value

    def set_points(self, value):
        self.points = value

    def set_home_bet(self, value):
        self.homeBet = value

    def set_away_bet(self, value):
        self.awayBet = value
