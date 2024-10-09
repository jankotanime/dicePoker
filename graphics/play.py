import variables as var


filler = """▏                                                             ▏\n"""

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
    2: """▏▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏""",
    3: "▏",
    4:"▏\n",
    5: "                                                             "
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


def playerUpTableForMore(player):
    print(player)
    dices = var.playersStatus[player]['dices']
    result = ""
    for i in range(1, 5):
        result += "▏         "
        for j in dices:
            result += dice[j][i]+"   "
        result += "       ▏\n"
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
            result += "   ^*^*^ "
        elif var.throwDices[i]:
            result += "   ***** "
        elif i+1 == var.currDice:
            result += "   ^^^^^ "
        else:
            result += "         "
    result += "▏\n"
    return result


def playersInside(playerLeft, playerRight):
    dicesLeft = var.playersStatus[playerLeft]['dices']
    result = ""
    if playerRight is not None:
        dicesRight = var.playersStatus[playerRight]['dices']
        for i in range(1, 21):
            result += "▏"
            result += dice[dicesLeft[(i-1)//4]][(i-1)%4+1]
            result += "                                                "
            result += dice[dicesRight[(i-1)//4]][(i - 1) % 4 + 1] + " ▏\n"
        result += 3*filler
    else:
        for i in range(1, 21):
            result += "▏"
            result += dice[dicesLeft[(i-1)//4]][(i-1)%4+1]
            result += "                                                       ▏\n"
        result += 3*filler



    return result


def displaying():
    if var.players[2] == 0:
        if var.currPlayer == 1:
            playerUp = 2
            playerDown = 1
        else:
            playerUp = 1
            playerDown = 2
        currWindow = (
            gameOutside[1]+
            playerUpTable(playerUp)+
            filler*17+
            playerDownTable(playerDown)+
            gameOutside[2]
        )
    else:
        if var.players[3] != 0:
            playerDown = (var.currPlayer - 1) % 4 + 1
            playerLeft = var.currPlayer % 4 + 1
            playerUp = (var.currPlayer + 1) % 4 + 1
            playerRight = (var.currPlayer + 2) % 4 + 1
        else:
            playerDown = (var.currPlayer - 1) % 3 + 1
            playerLeft = var.currPlayer % 3 + 1
            playerUp = (var.currPlayer + 1) % 3 + 1
            playerRight = None

        currWindow = (
            gameOutside[1]+
            playerUpTableForMore(playerUp)+
            playersInside(playerLeft, playerRight)+
            playerDownTable(playerDown)+
            gameOutside[2]
        )
    return currWindow
