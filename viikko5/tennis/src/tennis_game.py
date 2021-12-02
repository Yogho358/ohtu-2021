class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def score_name(self, score):
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"

    def even_score(self):
        if self.m_score1 < 4:
            score = self.m_score1
            return self.score_name(score) + "-All"
        else:
            return "Deuce"

    def advantage(self):
        if self.m_score1 - self.m_score2 == 1:
            return f"Advantage {self.player1_name}"
        if self.m_score1 - self.m_score2 >= 2:
            return f"Win for {self.player1_name}"
        if self.m_score2 - self.m_score1 == 1:
            return f"Advantage {self.player2_name}"
        if self.m_score2 - self.m_score1 >= 2:
            return f"Win for {self.player2_name}"

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return self.even_score()
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.advantage()
        else:
            return f"{self.score_name(self.m_score1)}-{self.score_name(self.m_score2)}"

