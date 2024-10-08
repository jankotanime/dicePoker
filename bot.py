import dicesManage
import playVariables as var
from collections import Counter


def move():
    thinking()
    dicesManage.moved()


def targeting(dices):
    zeroChange = [dicesManage.pointCount(dices), dices]
    oneChangeMax = [0, []]
    twoChangesMax = [0, []]
    threeChangesMax = [0, []]
    for i in range(5):
        for j in range(1, 7):
            newDices = dices[:]
            newDices[i] = j
            newDicesPoints = dicesManage.pointCount(newDices)
            if newDicesPoints > oneChangeMax[0]:
                oneChangeMax = [newDicesPoints, newDices]
            for k in range(5):
                for l in range(1, 7):
                    newDices = dices[:]
                    newDices[k] = l
                    newDicesPoints = dicesManage.pointCount(newDices)
                    if newDicesPoints > twoChangesMax[0]:
                        twoChangesMax = [newDicesPoints, newDices]
                    for m in range(5):
                        for n in range(1, 7):
                            newDices = dices[:]
                            newDices[m] = n
                            newDicesPoints = dicesManage.pointCount(newDices)
                            if newDicesPoints > threeChangesMax[0]:
                                threeChangesMax = [newDicesPoints, newDices]
    return [zeroChange, oneChangeMax, twoChangesMax, threeChangesMax]


def calculating(botDices, otherDices):
    scareScore = 1
    for i in otherDices:
        if botDices[3][0] < i[0][0] or botDices[3][0] < i[1][0]\
                or botDices[2][0] < otherDices[i][0][0]:
            return 0
        if botDices[1][0] < otherDices[i][0][0] or botDices[2][0] < otherDices[i][1][0]\
                or botDices[3][0] < otherDices[i][2][0]:
            scareScore -= 0.6 / len(otherDices)
        if botDices[0][0] < otherDices[i][0][0] or botDices[1][0] < otherDices[i][1][0]\
                or botDices[2][0] < otherDices[i][2][0] or botDices[3][0] < otherDices[i][3][0]:
            scareScore -= 0.2 / len(otherDices)
        if botDices[0][0] < otherDices[i][1][0] or botDices[1][0] < otherDices[i][2][0]\
                or botDices[2][0] < otherDices[i][3][0]:
            scareScore -= 0.2 / len(otherDices)
        if botDices[0][0] < otherDices[i][2][0] or botDices[1][0] < otherDices[i][3][0]:
            scareScore -= 0.2 / len(otherDices)
        if botDices[0][0] < otherDices[i][3][0]:
            scareScore -= 0.1 / len(otherDices)
    if scareScore <= 0:
        return 0
    else:
        return scareScore


def thinking():
    dices = var.playersStatus[var.currPlayer]["dices"]
    if dices == [None, None, None, None, None]:
        dicesManage.throwing([True, True, True, True, True])
    else:
        botPoints = targeting(dices)
        otherPoints = [targeting(var.playersStatus[i]["dices"]) for i in var.playersStatus if i != var.currPlayer]
        risk = calculating(botPoints, otherPoints)
        dicesToThrow = [botPoints[3][1][i] == dices[i] for i in range(5)]
        if risk != 0:
            dicesManage.throwing(dicesToThrow)
        else: print("pass")
