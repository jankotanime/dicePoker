import playVariables as var


filler = """▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏\n"""

dice = {
    None: {
        1: "▁▁▁▁▁ ",
        2: '▏    ▏',
        3: '▏    ▏',
        4: '☰☰☰☰☰ '
    },
    1: {
        1: "▁▁▁▁▁ ",
        2: '▏    ▏',
        3: '▏ ̇  ▏',
        4: '☰☰☰☰☰ '
    },
2: {
        1: "▁▁▁▁▁ ",
        2: '▏•   ▏',
        3: '▏  • ▏',
        4: '☰☰☰☰☰ '
    },
3: {
        1: "▁▁▁▁▁ ",
        2: '▏•   ▏',
        3: '▏ ̇• ▏',
        4: '☰☰☰☰☰ '
    },
4: {
        1: "▁▁▁▁▁ ",
        2: '▏• • ▏',
        3: '▏• • ▏',
        4: '☰☰☰☰☰ '
    },
5: {
        1: "▁▁▁▁▁ ",
        2: '▏• • ▏',
        3: '▏•̇• ▏',
        4: '☰☰☰☰☰ '
    },
6: {
        1: "▁▁▁▁▁ ",
        2: '▏••• ▏',
        3: '▏••• ▏',
        4: '☰☰☰☰☰ '
    }
}

gameOutside = {
    1: """▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n""",
    2: """▏▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏"""
}

gameInside = {
    1: (gameOutside[1] + """
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
""" + gameOutside[2]),
    2: (
            gameOutside[1] + """
▏▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁                ▏
▏▏    ▏  ▏•   ▏  ▏• • ▏  ▏• • ▏  ▏••• ▏  ▏•   ▏               ▏
▏▏ ̇  ▏  ▏  • ▏  ▏• • ▏  ▏•̇• ▏  ▏••• ▏  ▏ ̇• ▏               ▏
▏☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰                ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏             ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▁▁▁▁▁   ▏
▏             ▏    ▏  ▏•   ▏  ▏• • ▏  ▏• • ▏  ▏••• ▏  ▏•   ▏  ▏
▏             ▏ ̇  ▏  ▏  • ▏  ▏• • ▏  ▏•̇• ▏  ▏••• ▏  ▏ ̇• ▏  ▏
▏             ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ☰☰☰☰☰   ▏
""" + gameOutside[2]
    )
}


def playerUpTable(player):
    dices = var.playersStatus[player]['dices']
    result = ""
    for i in range(1, 5):
        result += "▏"
        for j in dices:
            result += dice[j][i]+"   "
        result += "                ▏\n"
    return result


def playerDownTable(player):
    dices = var.playersStatus[player]['dices']
    result = ""
    for i in range(1, 5):
        result += "▏                "
        for j in dices:
            result += "   "+dice[j][i]
        result += "▏\n"
    result += "▏                "
    for i in range(0, 5):
        if var.throwDices[i] and i+1 == var.currDice:
            result += "   ^~^^~^"
        elif var.throwDices[i]:
            result += "   ~~~~~~"
        elif i+1 == var.currDice:
            result += "   ^^^^^^"
        else:
            result += "         "
    result += "▏\n"
    return result


def displaying():
    if var.currPlayer == 1:
        playerUp = 2
        playerDown = 1
    else:
        playerUp = 1
        playerDown = 2
    currWindow = (
        gameOutside[1]+
        playerUpTable(playerUp)+
        filler+
        playerDownTable(playerDown)+
        gameOutside[2]
    )
    return currWindow
