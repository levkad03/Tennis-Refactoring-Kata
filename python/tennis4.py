# -*- coding: utf-8 -*-
TENNIS_PTS = ["Love", "Fifteen", "Thirty", "Forty"]
POINTS_3 = 3
POINTS_2 = 2
POINTS_1 = 1
MINUS = "-"
POINTS_4 = 4
ADVANTAGE = "Advantage "
WIN = "Win for "
DEUCE = "Deuce"
ALL = "-All"


class TennisGame4:
    def __init__(self, player1Name, player2Name):
        self.server = player1Name
        self.receiver = player2Name
        self.serverScore = 0
        self.receiverScore = 0

    def won_point(self, playerName):
        if self.server == playerName:
            self.serverScore += POINTS_1
        else:
            self.receiverScore += POINTS_1

    def score(self):
        result = Deuce(
            self, GameServer(
                self, GameReceiver(
                    self, AdvantageServer(
                        self, AdvantageReceiver(
                            self, DefaultResult(self)))))).getResult()
        return result.format()

    def receiverHasAdvantage(self):
        return self.receiverScore >= POINTS_4 and (self.receiverScore - self.serverScore) == POINTS_1

    def serverHasAdvantage(self):
        return self.serverScore >= POINTS_4 and (self.serverScore - self.receiverScore) == POINTS_1

    def receiverHasWon(self):
        return self.receiverScore >= POINTS_4 and (self.receiverScore - self.serverScore) >= POINTS_2

    def serverHasWon(self):
        return self.serverScore >= POINTS_4 and (self.serverScore - self.receiverScore) >= POINTS_2

    def isDeuce(self):
        return self.serverScore >= POINTS_3 and self.receiverScore >= POINTS_3 and (self.serverScore == self.receiverScore)


class TennisResult:
    def __init__(self, serverScore, receiverScore):
        self.serverScore = serverScore
        self.receiverScore = receiverScore

    def format(self):
        if "" == self.receiverScore:
            return self.serverScore
        if self.serverScore == self.receiverScore:
            return self.serverScore + ALL
        return self.serverScore + MINUS + self.receiverScore


class Deuce:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if self.game.isDeuce():
            return TennisResult(DEUCE, "")
        return self.nextResult.getResult()


class GameServer:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if self.game.serverHasWon():
            return TennisResult(WIN + self.game.server, "")
        return self.nextResult.getResult()


class GameReceiver:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if self.game.receiverHasWon():
            return TennisResult(WIN + self.game.receiver, "")
        return self.nextResult.getResult()


class AdvantageServer:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if self.game.serverHasAdvantage():
            return TennisResult(ADVANTAGE + self.game.server, "")
        return self.nextResult.getResult()


class AdvantageReceiver:
    def __init__(self, game, nextResult):
        self.game = game
        self.nextResult = nextResult

    def getResult(self):
        if self.game.receiverHasAdvantage():
            return TennisResult(ADVANTAGE + self.game.receiver, "")
        return self.nextResult.getResult()


class DefaultResult:
    def __init__(self, game):
        self.game = game
        self.scores = TENNIS_PTS

    def getResult(self):
        return TennisResult(self.scores[self.game.serverScore], self.scores[self.game.receiverScore])
