# -*- coding: utf-8 -*-
POINTS_6 = 6
POINTS_4 = 4
WIN = "Win for "
ADVANTAGE = "Advantage "
DEUCE = "Deuce"
MINUS = "-"
ALL = "-All"


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.player1_name = player1Name
        self.player2_name = player2Name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, name):
        if name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if (self.player1_points < POINTS_4 and self.player2_points < POINTS_4) and (self.player1_points +
                                                                                    self.player2_points < POINTS_6):
            tennis_pts = ["Love", "Fifteen", "Thirty", "Forty"]
            score = tennis_pts[self.player1_points]
            return score + ALL if (self.player1_points == self.player2_points) \
                else score + MINUS + tennis_pts[self.player2_points]
        else:
            if self.player1_points == self.player2_points:
                return DEUCE
            score = self.player1_name if self.player1_points > self.player2_points else self.player2_name
            return ADVANTAGE + score if ((self.player1_points - self.player2_points) *
                                         (self.player1_points - self.player2_points) == 1) else WIN + score
