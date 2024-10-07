import playVariables as var
import random
from collections import Counter


def pointCount(player):
    actPoints = 0
    dices = player["dices"]
    if {1, 2, 3, 4, 5}.issubset(dices) or {2, 3, 4, 5, 6}.issubset(dices):
        actPoints += 13+sum(dices)/100
    else:
        dice = Counter(dices)
        for i in dice.keys():
            actPoints += i**(1/10)*(dice[i]**2)
    player["points"] = actPoints


def moved():
    pointCount(var.playersStatus[var.currPlayer])
    var.playersStatus[var.currPlayer]["moves"] -= 1
    if var.players[var.currPlayer] and var.players[var.currPlayer] != 0:
        var.currPlayer = var.currPlayer + 1
    else:
        var.currPlayer = 1
    if var.playersStatus[var.currPlayer]["moves"] == 3:
        var.throwDices = [True, True, True, True, True]
    else:
        var.throwDices = [False, False, False, False, False]


def randomNumber():
    result = random.randint(1, 6)
    return result


def throwing(dices):
    for i in range(0, 5):
        if dices[i]:
            var.playersStatus[var.currPlayer]["dices"][i] = randomNumber()
