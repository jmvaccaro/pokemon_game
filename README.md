# Pokémon Rock, Paper, Scissors Game

This is a Pokémon-themed version of the classic "Rock, Paper, Scissors" game. In this version, the three basic options—Rock, Paper, and Scissors— are replaced with Pokémon types: **Fire**, **Water**, and **Leaf**. Players choose one of these Pokémon types, and the game randomly selects the rival's choice. The objective is to win the game by earning more points in a series of rounds, where each type beats one other type and loses to the third type.

## How to Play

1. **Choose Your Pokémon**: You can choose between Fire, Water, or Leaf by clicking on the corresponding button. Each button is associated with a different Pokémon from the Pokémon series.
   
2. **Rounds**: The game proceeds in rounds. After you make a selection, the computer randomly selects a rival Pokémon, and the winner of the round is determined based on the type advantages:
   - **Fire** beats **Leaf**.
   - **Water** beats **Fire**.
   - **Leaf** beats **Water**.
   
3. **Scores**: The scores for both players are displayed as stars (**★**). The first player to reach the target score (3 victories) wins the game.

4. **Continue to Next Round**: After each round, you will need to click the "Continue" button to proceed to the next round.

5. **Winning the Game**: The game ends when one of the players accumulates 3 victories. The winner is displayed with a victory message.

## Features

- **Interactive GUI**: The game is powered by a graphical user interface (GUI) using **Tkinter**. Images for each Pokémon type (Fire, Water, and Leaf) are displayed alongside the player's and rival's selections.
- **Random Rival Choices**: The rival Pokémon is chosen randomly each round, making the game unpredictable and fun.
- **Score Tracking**: The score is dynamically updated as you win or lose rounds, with the winner of the game being announced once 3 victories are achieved.

## Requirements

- Python 3.x
- Tkinter (for the GUI)
- Pillow (for image handling)

## How to Run

1. Clone this repository to your local machine.
2. Install the necessary Python libraries (Tkinter and Pillow).
3. Run the Python script to start the game.

```bash
git clone https://github.com/jmvaccaro/pokemon_game.git
cd pokemon_game
python pokemon_game.py
