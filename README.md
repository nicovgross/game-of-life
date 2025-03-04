# Game of Life

Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), using the Pygame library to display and interact with the game.

![image](https://github.com/user-attachments/assets/39b42ffa-c48a-427f-a548-251627faf3b0)

Running
=======
Requires Python 3.7+, Numpy and Pygame

If not installed, run:
```bash
pip install -r requirements.txt
```

To run Game of Life:
```bash
python game-of-life.py
```

# Controls
The game controls are specified in "controls.txt"


# How it works
The game board is a simple n by n numpy array, and its cells can assume a value of either 1 or 0, with 1 meaning alive and 0 meaning dead. The game starts with an initial configuration, that is chosen by the player, and the evolution of the game depends solely on this initial state. In each iteration, the program counts the number of live neighboring cells of each cell and updates the board based on that number.
