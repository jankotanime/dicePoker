import variables as var
import random
from collections import Counter


# Counting amount of points that are given to dices combination
def pointCount(dices):
    if None in dices:
        return 0
    actPoints = 0
    if {1, 2, 3, 4, 5}.issubset(dices) or {2, 3, 4, 5, 6}.issubset(dices):
        actPoints += 13+sum(dices)/100
    else:
        dice = Counter(dices)
        for i in dice.keys():
            actPoints += int(i)**(1/10)*(dice[i]**2)
    return actPoints


# Checking if the player really want to pass
def passing(event):
    var.passing = False
    if event == 'enter':
        var.playersStatus[var.currPlayer]["moves"] = 0
        moved()


# Function that inform program that player has moved: changing actual player, arrangement of dices etc.
def moved():
    var.wantToBet = 0
    var.playersStatus[var.currPlayer]["points"] = pointCount(var.playersStatus[var.currPlayer]["dices"])
    var.playersStatus[var.currPlayer]["moves"] -= 1
    var.fullTable = sum([var.playersStatus[i]["table"] for i in var.playersStatus])
    if len(var.players) > var.currPlayer and var.players[var.currPlayer] != 0:
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


# Randomizing thrown dices
def throwing(dices):
    for i in range(0, 5):
        if dices[i]:
            var.playersStatus[var.currPlayer]["dices"][i] = randomNumber()
