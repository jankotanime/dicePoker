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

how_to_play = {
    1: """▏                                                             ▏
▏1. The goal is to amass the biggest amount of money          ▏
▏2. Every player has 3 turns to roll any of their dice        ▏
▏3. If a player has on table less money than previous bet,    ▏
▏   they must raise the stakes to still play                  ▏
▏4. If a player passes he lost all money he put on table      ▏
▏5. You cannot bet 0 money                                    ▏\n""",
    2: """▏Points counting:                                             ▏
▏The strongest dice configuration is five of kind,            ▏
▏second strongest is four of kind, next is straight,          ▏
▏after that there is full house, three of kind, two of kind   ▏
▏and the last one is hight dice.                              ▏
▏                                                             ▏
▏ For example:                                                ▏
▏ ⚅ ⚅ ⚅ ⚅ ⚅ > ⚀ ⚀ ⚀ ⚀ ⚀ > ⚅ ⚅ ⚅ ⚅ ⚄ > ⚀ ⚀ ⚀ ⚀ ⚁ > ⚁ ⚂ ⚃ ⚄ ⚅  ▏
▏ ⚁ ⚂ ⚃ ⚄ ⚅ > ⚀ ⚁ ⚂ ⚃ ⚄ > ⚅ ⚅ ⚅ ⚄ ⚄ > ⚀ ⚀ ⚀ ⚁ ⚁ > ⚅ ⚅ ⚅ ⚄ ⚃  ▏
▏ ⚅ ⚅ ⚅ ⚄ ⚃ > ⚀ ⚀ ⚀ ⚁ ⚂ > ⚅ ⚅ ⚂ ⚃ ⚄ > ⚀ ⚀ ⚁ ⚂ ⚃ > ⚀ ⚂ ⚃ ⚄ ⚅  ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏\n"""
}

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
    if var.menuStatus == 4:
        result += how_to_play[1]
        result += filler*16
        result += how_to_play[2]
    else:
        result += filler*5
        result += logo
        result += filler*3
        if var.menuStatus < 4:
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
