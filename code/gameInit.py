# Game starting and ending functions
import variables as var
import display
import graphics.play as graphic
import graphics.menu as menu


def initing():
    var.menuStatus = 1
    var.currPlayer = 1
    var.currDice = 1
    var.throwDices = [True, True, True, True, True]
    var.passing = False
    var.playersStatus = {}
    var.players.sort(reverse=True)
    for i in var.players:
        if i != 0:
            position = len(var.playersStatus)+1
            var.playersStatus[position] = {
                "dices": [None, None, None, None, None],
                "points": 0,
                "moves": 3,
                "table": 0
            }
            if i == 2:
                var.playersStatus[position]["playerType"] = "player"
                if var.difficulty == 1:
                    var.playersStatus[position]["cash"] = 2000
                else:
                    var.playersStatus[position]["cash"] = 1000
            elif i == 1:
                var.playersStatus[position]["playerType"] = "bot"
                if var.difficulty == 1 or var.difficulty == 2:
                    var.playersStatus[position]["cash"] = 1000
                else:
                    var.playersStatus[position]["cash"] = 2000
    display.displaying(graphic.displaying())


def continuing():
    var.menuStatus = 1
    var.currPlayer = 1
    var.currDice = 1
    var.throwDices = [True, True, True, True, True]
    var.passing = False
    for player in var.playersStatus:
        var.playersStatus[player]["dices"] = [None, None, None, None, None]
        var.playersStatus[player]["points"] = 0
        var.playersStatus[player]["moves"] = 3
        var.playersStatus[player]["table"] = 0
    display.displaying(graphic.displaying())

def endGame():
    var.endScreen = True
    var.play = False
    var.menuStatus = 1
    winner = max(var.playersStatus, key=lambda x: var.playersStatus[x]["points"])
    var.playersStatus[winner]["cash"] += var.fullTable
    var.fullTable = 0
    display.displaying(menu.displaying())
