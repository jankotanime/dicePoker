import playVariables as var
import display
import graphics.play as graphic


def initing():
    for i in var.players:
        if i != 0:
            position = len(var.playersStatus)+1
            var.playersStatus[position] = {
                "dices": [None, None, None, None, None],
                "points": 0,
                "moves": 3,
                "table": 0
            }
            if i == 1:
                var.playersStatus[position]["playerType"] = "player"
                if var.difficulty == 1:
                    var.playersStatus[position]["cash"] = 2000
                else:
                    var.playersStatus[position]["cash"] = 1000
            elif i == 2:
                var.playersStatus[position]["playerType"] = "bot"
                if var.difficulty == 1 or var.difficulty == 2:
                    var.playersStatus[position]["cash"] = 1000
                else:
                    var.playersStatus[position]["cash"] = 2000
    display.displaying(graphic.displaying())
