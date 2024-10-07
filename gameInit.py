import playVariables as var
import display
import graphics.play as graphic

def initing():
    for i in var.players:
        position = len(var.playersStatus)
        if i == 1:
            var.playersStatus[position] = {
                "dices": [None, None, None, None, None],
                "points": 0,
                "pass": False,
                "playerType": "player",
                "table": 0
            }
            if var.difficulty == 1:
                var.playersStatus[position]["cash"] = 2000
            else:
                var.playersStatus[position]["cash"] = 1000
        elif i == 2:
            var.playersStatus[position] = {
                "dices": [None, None, None, None, None],
                "points": 0,
                "cash": 0,
                "pass": False,
                "table": 0,
                "playerType": "player"
            }
            if var.difficulty == 1 or var.difficulty == 2:
                var.playersStatus[position]["cash"] = 1000
            else:
                var.playersStatus[position]["cash"] = 2000
    display.displaying(graphic.gameInside[2])
