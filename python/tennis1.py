# -*- coding: utf-8 -*-
POINTS_1 = 1
MINUS = "-"
MINUS_RES_2 = 2
MINUS_RES_MINUS_1 = -1
MINUS_RES_1 = 1
POINTS_4 = 4
FORTY = "Forty"
THIRTY = "Thirty"
FIFTEEN = "Fifteen"
LOVE = "Love"

WIN_PLAYER_2 = "Win for player2"
WIN_PLAYER_1 = "Win for player1"
ADVANTAGE_PLAYER_2 = "Advantage player2"
ADVANTAGE_PLAYER_1 = "Advantage player1"
DEUCE = "Deuce"
THIRTY_ALL = "Thirty-All"
FIFTEEN_ALL = "Fifteen-All"
LOVE_ALL = "Love-All"

PTS_ALL = {
    0: LOVE_ALL,
    1: FIFTEEN_ALL,
    2: THIRTY_ALL,
}

TENNIS_PTS = {
    0: LOVE,
    1: FIFTEEN,
    2: THIRTY,
    3: FORTY,
}


class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += POINTS_1
        else:
            self.p2points += POINTS_1

    def score(self):
        result = ""
        tempScore = 0
        if self.p1points == self.p2points:
            result = PTS_ALL.get(self.p1points, DEUCE)
        elif self.p1points >= POINTS_4 or self.p2points >= POINTS_4:
            minusResult = self.p1points - self.p2points
            result = self.check_player_advantage(minusResult)
        else:
            result = self.get_tennis_score(result)
        return result

    def get_tennis_score(self, result):
        player_scores = [self.p1points, self.p2points]
        result = MINUS.join(TENNIS_PTS[tempScore] for tempScore in player_scores)
        return result

    def check_player_advantage(self, minusResult):
        if minusResult == MINUS_RES_1:
            result = ADVANTAGE_PLAYER_1
        elif minusResult == MINUS_RES_MINUS_1:
            result = ADVANTAGE_PLAYER_2
        elif minusResult >= MINUS_RES_2:
            result = WIN_PLAYER_1
        else:
            result = WIN_PLAYER_2
        return result
