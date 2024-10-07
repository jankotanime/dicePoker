import playVariables as var
import random


def randomNumber():
    result = random.randint(1, 6)
    return result


def throwing(dices):
    for i in range(0, 5):
        if dices[i]:
            var.playersStatus[var.currPlayer]["dices"][i] = randomNumber()
