import dices
import playVariables as var


def move():
    dices.throwing([True, True, True, True, True])
    dices.moved()


def thinking():
    dices = var.playersStatus[var.currPlayer]["dices"]