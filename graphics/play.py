import variables as var


dice = {
    None: {
        1: "      ",
        2: '      ',
        3: '      ',
        4: '      '
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

filler = """▏                                                             ▏\n"""
start = "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n"
end = "▏▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏"

def statistics(player, i):
    result = ""
    if i == 1:
        lane = str(var.wantToBet)
        result += "Bet: " + lane + (9-len(lane))*" "
    elif i == 2:
        lane = str(round(player["points"], 2))
        result += "Points: " + lane + (6-len(lane))*" "
    elif i == 3:
        lane = str(player["cash"])
        result += "Cash: " + lane + (8-len(lane))*" "
    elif i == 4:
        lane = str(player["table"])
        result += "Table: " + lane + (7-len(lane))*" "
    return result

def center(i):
    panel = {
        10: "    DICE POKER       ",
        11: "                     ",
        12: "   ON TABLE: " + str(var.fullTable) + (8-len(str(var.fullTable)))*" "
    }
    if var.playersStatus[var.currPlayer]['playerType'] == 'bot':
        panel[13] = "    BOT IS MOVING    "
    elif var.endScreen:
        panel[13] = " END OF THE GAME     "
    elif var.passing:
        panel[13] = " PRESS ENTER TO PASS "
    elif var.playersStatus[var.currPlayer]['playerType'] == 'player':
        panel[13] = "CHOOSE DICES TO THROW"
    if var.endScreen:
        panel[14] = "  WINNER: Player "+str(max(var.playersStatus, key=lambda x: var.playersStatus[x]["points"]))+"   "
    else:
        panel[14] = "                     "
    return panel[i]

def player_up_table(player):
    dices = player['dices']
    result = ""
    for i in range(1, 5):
        result += "▏"
        for j in dices:
            result += dice[j][i]+"   "
        if i == 2:
            lane = str(player["cash"])
            result += "Cash: " + lane + (4-len(lane))*" " + "      ▏\n"
        elif i == 3:
            lane = str(round(player["points"], 2))
            result += "Points: " + lane + (7-len(lane))*" " + " ▏\n"
        elif i == 4:
            lane = str(player["table"])
            result += "Table: " + lane + (8-len(lane))*" " + " ▏\n"
        else:
            result += "                ▏\n"
    return result

def players_inside(player_left, player_right):
    if player_left is not None:
        dices_left = var.playersStatus[player_left]['dices']
    else: 
        dices_left = [None, None, None, None, None]
    if player_right is not None:
        dices_right = var.playersStatus[player_right]['dices']
    else:
        dices_right = [None, None, None, None, None]
    result = ""
    for i in range(1, 21):
        result += "▏"
        result += dice[dices_left[(i-1)//4]][(i-1)%4+1]
        if player_left is not None and i in [2, 3, 4]:
            result += statistics(var.playersStatus[player_left], i)
        else:
            result += "              "
        if i in range(10, 15):
            result += center(i)
        else:
            result += "                     "
        if player_right is not None and i in [2, 3, 4]:
            result += statistics(var.playersStatus[player_right], i)
        else:
            result += "              "
        result += dice[dices_right[(i-1)//4]][(i-1)%4+1]
        result += "▏\n"
    return result

def player_down_table(player):
    dices = player['dices']
    result = ""
    for i in range(1, 5):
        result += "▏  "
        result += statistics(player, 5-i)
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

def displaying():
    result = start
    player_left = None
    player_right = None
    if var.players[2] == 0:
        player_up = (var.currPlayer) % 2 + 1
        player_down = (var.currPlayer - 1) % 2 + 1
    elif var.players[3] == 0:
        player_down = (var.currPlayer - 1) % 3 + 1
        player_left = var.currPlayer % 3 + 1
        player_up = (var.currPlayer + 1) % 3 + 1
    else:
        player_down = (var.currPlayer - 1) % 4 + 1
        player_left = var.currPlayer % 4 + 1
        player_up = (var.currPlayer + 1) % 4 + 1
        player_right = (var.currPlayer + 2) % 4 + 1
    result += player_up_table(var.playersStatus[player_up])
    result += filler
    result += players_inside(player_left, player_right)
    result += filler * 2
    result += player_down_table(var.playersStatus[player_down])
    result += end
    return result