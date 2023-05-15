# -*- coding: utf-8 -*-
POINT_1 = 1
POINT_2 = 2
POINT_3 = 3
POINT_4 = 4

WIN_PLAYER_2 = "Win for player2"
WIN_PLAYER_1 = "Win for player1"

ADVANTAGE_PLAYER_1 = "Advantage player1"
ADVANTAGE_PLAYER_2 = "Advantage player2"

MINUS = "-"
ALL = "-All"
LOVE = "Love"
FIFTEEN = "Fifteen"
THIRTY = "Thirty"
FORTY = "Forty"
DEUCE = "Deuce"

TENNIS_PTS = {
    0: LOVE,
    1: FIFTEEN,
    2: THIRTY,
    3: FORTY,
}


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        result = self.all_or_deuce(result)
        result = self.def_love(result)
        result = self.update_pts(result)
        result = self.player_advantage(result)
        result = self.winner(result)
        return result

    def all_or_deuce(self, result):
        if self.p1points == self.p2points and self.p1points < POINT_3:
            result = TENNIS_PTS.get(self.p1points, "") + ALL
        if self.p1points == self.p2points and self.p1points > POINT_2:
            result = DEUCE
        return result

    def def_love(self, result):
        player2_game_to_zero = self.p1points > 0 and self.p2points == 0
        player1_game_to_zero = self.p2points > 0 and self.p1points == 0
        if player2_game_to_zero:
            P1res, P2res, result = self.player_pts(result)
        elif player1_game_to_zero:
            P1res, P2res, result = self.player_pts(result)
        return result

    def update_pts(self, result):
        if self.p2points < self.p1points < POINT_4:
            P1res, P2res, result = self.player_pts(result)
        if self.p1points < self.p2points < POINT_4:
            P1res, P2res, result = self.player_pts(result)
        return result

    def player_advantage(self, result):
        if self.p1points > self.p2points >= POINT_3:
            result = ADVANTAGE_PLAYER_1
        elif self.p2points > self.p1points >= POINT_3:
            result = ADVANTAGE_PLAYER_2
        return result

    def winner(self, result):
        score_difference = self.p1points - self.p2points

        if self.p1points >= POINT_4 and score_difference >= POINT_2:
            result = WIN_PLAYER_1
        elif self.p2points >= POINT_4 and -score_difference >= POINT_2:
            result = WIN_PLAYER_2
        return result

    def player_pts(self, result):
        P1res = TENNIS_PTS.get(self.p1points, "")
        P2res = TENNIS_PTS.get(self.p2points, "")
        result = P1res + MINUS + P2res
        return P1res, P2res, result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += POINT_1

    def P2Score(self):
        self.p2points += POINT_1
