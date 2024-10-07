import playVariables as playVar
import variables as var

mainMenuOutside = {
    1: ["""▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                       ==========                            ▏
▏                    || Dice Poker ||                         ▏
▏                       ==========                            ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏""",
        """▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏"""
        ],
    2: ["""▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                       ==========                            ▏
▏                    || Dice Poker ||                         ▏
▏                       ==========                            ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏""",
        """▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏                                                             ▏
▏▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏"""]
}

playersStatus = {
    0: "Closed",
    1: "Player",
    2: "Bot   "
}

diffStatus = {
    1: "---Easy---",
    2: "--Normal--",
    3: "---Hard---",
    4: "Impossible"
}


def displaying(status):
    mainMenu = {
        1: (mainMenuOutside[1][0] +
            """
▏                        ▶ Play ◀                             ▏
▏                                                             ▏
▏                      How to play?                           ▏
""" + mainMenuOutside[1][1]
            ),
        2: (mainMenuOutside[1][0]+"""
▏                          Play                               ▏
▏                                                             ▏
▏                    ▶ How to play? ◀                         ▏
"""+mainMenuOutside[1][1]),
        3: ("trzecia"),
        4: (""),
        5: (mainMenuOutside[2][0]+"""
▏                  ◀ Difficulty: """+diffStatus[playVar.difficulty]+""" ▶                 ▏
▏                                                             ▏
▏                                                             ▏
▏                    Player 1: """+playersStatus[playVar.players[0]]+"""                         ▏
▏                    Player 2: """+playersStatus[playVar.players[1]]+"""                         ▏
▏                    Player 3: """+playersStatus[playVar.players[2]]+"""                         ▏
▏                    Player 4: """+playersStatus[playVar.players[3]]+"""                         ▏
▏                                                             ▏
▏                                                             ▏
▏                         Start                               ▏
"""+mainMenuOutside[2][1]),
        6: (mainMenuOutside[2][0]+"""
▏                   Difficulty: """+diffStatus[playVar.difficulty]+"""                    ▏
▏                                                             ▏
▏                                                             ▏
▏                 ◀  Player 1: """+playersStatus[playVar.players[0]]+""" ▶                       ▏
▏                    Player 2: """+playersStatus[playVar.players[1]]+"""                         ▏
▏                    Player 3: """+playersStatus[playVar.players[2]]+"""                         ▏
▏                    Player 4: """+playersStatus[playVar.players[3]]+"""                         ▏
▏                                                             ▏
▏                                                             ▏
▏                         Start                               ▏
"""+mainMenuOutside[2][1]),
        7: (mainMenuOutside[2][0]+"""
▏                    Difficulty: """+diffStatus[playVar.difficulty]+"""                   ▏
▏                                                             ▏
▏                                                             ▏
▏                    Player 1: """+playersStatus[playVar.players[0]]+"""                         ▏
▏                  ◀ Player 2: """+playersStatus[playVar.players[1]]+""" ▶                       ▏
▏                    Player 3: """+playersStatus[playVar.players[2]]+"""                         ▏
▏                    Player 4: """+playersStatus[playVar.players[3]]+"""                         ▏
▏                                                             ▏
▏                                                             ▏
▏                         Start                               ▏
"""+mainMenuOutside[2][1]),
        8: (mainMenuOutside[2][0]+"""
▏                    Difficulty: """+diffStatus[playVar.difficulty]+"""                   ▏
▏                                                             ▏
▏                                                             ▏
▏                    Player 1: """+playersStatus[playVar.players[0]]+"""                         ▏
▏                    Player 2: """+playersStatus[playVar.players[1]]+"""                         ▏
▏                  ◀ Player 3: """+playersStatus[playVar.players[2]]+""" ▶                       ▏
▏                    Player 4: """+playersStatus[playVar.players[3]]+"""                         ▏
▏                                                             ▏
▏                                                             ▏
▏                         Start                               ▏
"""+mainMenuOutside[2][1]),
        9: (mainMenuOutside[2][0]+"""
▏                    Difficulty: """+diffStatus[playVar.difficulty]+"""                   ▏
▏                                                             ▏
▏                                                             ▏
▏                    Player 1: """+playersStatus[playVar.players[0]]+"""                         ▏
▏                    Player 2: """+playersStatus[playVar.players[1]]+"""                         ▏
▏                    Player 3: """+playersStatus[playVar.players[2]]+"""                         ▏
▏                  ◀ Player 4: """+playersStatus[playVar.players[3]]+""" ▶                       ▏
▏                                                             ▏
▏                                                             ▏
▏                         Start                               ▏
"""+mainMenuOutside[2][1]),
        10: (mainMenuOutside[2][0]+"""
▏                    Difficulty: """+diffStatus[playVar.difficulty]+"""                   ▏
▏                                                             ▏
▏                                                             ▏
▏                    Player 1: """+playersStatus[playVar.players[0]]+"""                         ▏
▏                    Player 2: """+playersStatus[playVar.players[1]]+"""                         ▏
▏                    Player 3: """+playersStatus[playVar.players[2]]+"""                         ▏
▏                    Player 4: """+playersStatus[playVar.players[3]]+"""                         ▏
▏                                                             ▏
▏                                                             ▏
▏                       ▶ Start ◀                             ▏
"""+mainMenuOutside[2][1])
    }
    return mainMenu[status]