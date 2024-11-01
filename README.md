# Dice Poker
### Version: Alfa 1.0

---

## Description
**Dice Poker** is simple terminal-based game for single or multiplayer modes, where objective is to accumulate the most money. The game supports up to 4 players, and each player can be either bot or a human. This project was developed to practice and maintain Python programming skills.

## Requirements
- Python 3.8+
- Libraries: os, keyboard, random

## How To Play
### Controls:
- To leave the game press esc
- Menu: 
    - Navigate: arrow keys (up and down)
    - Deciding: space or enter
- Game:
    - Betting: arrow keys (up and down)
    - Navigate through the dices: arrow keys (left and right)
    - Choosing a dice to throw: space
    - Throwing: enter
    - Passing: q
    - Va banque: v

### Rules
The goal is to amass the biggest amount of money but mostly is to not losing them. Every player has 3 turns to roll any of their dice. If a player has on table less money than previous bet, they must either raise the stakes or pass, losing all their current round bets. 

## Game Features
- Full Game Flow: Possible constant game, not only ties. Players can remain their money.
- AI Bots: Bots with complex decision-making processes. They calculate their chances of winning based on remaining money and game conditions.
- Betting: Players can call, raise the stakes, pass or play Va banque.
- Console Graphics: The game uses terminal-based graphics and objects to display the current state of the game each round. Not library used.
