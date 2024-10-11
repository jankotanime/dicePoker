import dicesManage as dices
import variables as var
import display
import graphics.play as graphic
import bot
import gameInit as init


# Processing what human player want to do or if the player is computer it makes him to move
def movement(event):
    if var.playersStatus[var.currPlayer]["playerType"] == "player":
        if not var.passing:
            accCash = var.playersStatus[var.currPlayer]["cash"]
            accTable = var.playersStatus[var.currPlayer]["table"]
            if event == 'space':
                var.throwDices[var.currDice-1] = not var.throwDices[var.currDice-1]
            elif event == 'enter':
                onTableCash = [var.playersStatus[i]["table"] for i in var.playersStatus]
                if accTable + var.wantToBet > 0 and var.wantToBet + accTable >= max(onTableCash):
                    var.playersStatus[var.currPlayer]["table"] += var.wantToBet
                    var.playersStatus[var.currPlayer]["cash"] -= var.wantToBet
                    dices.throwing(var.throwDices)
                    dices.moved()
                else:
                    "Not enough on table"
            elif event == 'left' and var.currDice != 1:
                var.currDice -= 1
            elif event == 'right' and var.currDice != 5:
                var.currDice += 1
            elif event == 'up' and 10+var.wantToBet <= accCash:
                var.wantToBet += 10
            elif event == 'down' and var.wantToBet-10 > 0:
                var.wantToBet -= 10
            elif event == 'q':
                var.passing = True
        else:
            dices.passing(event)
    else:
        bot.move()


def actPlayer():
    return var.playersStatus[var.currPlayer]


def tick(event):
    isAnyPlayer = any(var.playersStatus[x]["moves"] > 0 for x in var.playersStatus)
    if not isAnyPlayer:
        init.endGame()
    elif actPlayer()["moves"] > 0:
        movement(event)
        display.displaying(graphic.displaying())
        if actPlayer()["playerType"] == "bot":
            tick(None)
    else:
        dices.moved()
        tick(None)
    display.displaying(graphic.displaying())
