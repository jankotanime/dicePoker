import dicesManage
import variables as var


def move():
    thinking()


def targeting(dices):
    if dices == [None, None, None, None, None]:
        dices = [1, 2, 3, 3, 4]
    zeroChange = [dicesManage.pointCount(dices), dices]
    oneChangeMax = [0, []]
    twoChangesMax = [0, []]
    for i in range(5):
        for j in range(1, 7):
            newDices1 = dices[:]
            newDices1[i] = j
            newDicesPoints = dicesManage.pointCount(newDices1)
            if newDicesPoints > oneChangeMax[0]:
                oneChangeMax = [newDicesPoints, newDices1]
            for k in range(5):
                for l in range(1, 7):
                    newDices2 = newDices1[:]
                    newDices2[k] = l
                    newDicesPoints = dicesManage.pointCount(newDices2)
                    if newDicesPoints > twoChangesMax[0]:
                        twoChangesMax = [newDicesPoints, newDices2]
    return [zeroChange, oneChangeMax, twoChangesMax]


def calculating(botDices, otherDices):
    scareScore = 1
    for i in otherDices:
        if botDices[2][0] < i[0][0]:
            return 0
        if botDices[1][0] < i[0][0] or botDices[2][0] < i[1][0]:
            scareScore -= 0.3
        if botDices[0][0] < i[0][0] or botDices[1][0] < i[1][0]\
                or botDices[2][0] < i[2][0]:
            scareScore -= 0.2
        if botDices[0][0] < i[1][0] or botDices[1][0] < i[2][0]:
            scareScore -= 0.2 / len(otherDices)
        if botDices[0][0] < i[2][0]:
            scareScore -= 0.1 / len(otherDices)
    if scareScore <= 0:
        return 0
    else:
        return scareScore


def chosingToThrow(dices, botPoints):
    if botPoints[2][0]+3 >= dicesManage.pointCount(dices):
        dicesToThrow = [botPoints[2][1][i] != dices[i] for i in range(5)]
    elif botPoints[1][0]+3 >= targeting(dices):
        dicesToThrow = [botPoints[1][1][i] != dices[i] for i in range(5)]
    else:
        dicesToThrow = [False, False, False, False, False]
    return dicesToThrow


def beting(dices):
    botPoints = targeting(dices)
    otherPoints = [targeting(var.playersStatus[i]["dices"]) for i in var.playersStatus if {i} != var.currPlayer]
    risk = calculating(botPoints, otherPoints)
    dicesToThrow = chosingToThrow(dices, botPoints)
    onTableCash = [var.playersStatus[i]["table"] for i in var.playersStatus]
    diff = (risk**(var.playersStatus[var.currPlayer]["moves"])/3) * (var.playersStatus[var.currPlayer]["cash"] + var.playersStatus[var.currPlayer]["table"])
    if diff >= max(onTableCash):
        var.playersStatus[var.currPlayer]["cash"] -= diff
        var.playersStatus[var.currPlayer]["table"] += diff
        dicesManage.throwing(dicesToThrow)
        dicesManage.moved()
    else:
        dicesManage.passing('enter')


def thinking():
    dices = var.playersStatus[var.currPlayer]["dices"]
    if dices == [None, None, None, None, None]:
        dicesManage.throwing([True, True, True, True, True])
    else:
        beting(dices)

# To add: if the bot have dices (ex.) 1, 1, 4, 5, 6 he decides to throw only 4 and 5, but should be throwing 4, 5, 6
