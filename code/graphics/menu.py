import variables as var

players_status = {
    0: "Closed",
    1: "Bot   ",
    2: "Player"
}

diff_status = {
    1: "---Easy---",
    2: "--Normal--",
    3: "---Hard---",
    4: "Impossible"
}

def lines(number): 
    result = {
        1: "Continue",
        2: "Play",
        3: "How to play?",
        5: "Difficulty: " + diff_status[var.difficulty],
        6: "Player 1: " + players_status[var.players[0]],
        7: "Player 2: " + players_status[var.players[1]],
        8: "Player 3: " + players_status[var.players[2]],
        9: "Player 4: " + players_status[var.players[3]],
        10: "Start"
    }
    return result[number]

start = "▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁\n"
end = "▏▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏"
filler = "▏                                                             ▏\n"
logo = """▏                         ==========                          ▏
▏                      || Dice Poker ||                       ▏
▏                         ==========                          ▏\n"""


def select(line, line_number):
    result = "▏"
    result += ((57 - len(line))//2)*" "
    if var.menuStatus == line_number:
        result += "▶ " + line + " ◀"
    else:
        result += "  " + line + "  "
    result += ((58 - len(line)) // 2) * " "
    result += "▏\n"
    return result


def displaying():
    result = start
    result += filler*5
    result += logo
    result += filler*3
    if var.menuStatus < 5:
        for i in range(1, 4):
            result += select(lines(i), i)
            result += filler
        result += filler*15
    else:
        for i in range(5, 11):
            result += select(lines(i), i)
            if i == 5 or i == 9:
                result += filler
        result += filler*13
    result += end
    return result
