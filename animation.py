import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Inicializa o tabuleiro
def initialize_board(n):
    board = np.zeros([n, n])
    return board

# Verifica os vizinhos
def check_neighbors(board, cell):
    live_neighbors = 0
    i, j = cell
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                 (1, 1), (1, 0), (1, -1), (0, -1)]
    for dx, dy in neighbors:
        x, y = i + dx, j + dy
        if 0 <= x < board.shape[0] and 0 <= y < board.shape[1] and board[x, y] == 1:
            live_neighbors += 1
    return live_neighbors

# Atualiza o tabuleiro
def update_board(prev_board):
    n = prev_board.shape[0]
    new_board = initialize_board(n)
    for i in range(n):
        for j in range(n):
            live_neighbors = check_neighbors(prev_board, (i, j))
            if prev_board[i, j] == 1 and live_neighbors in [2, 3]:
                new_board[i, j] = 1
            elif prev_board[i, j] == 0 and live_neighbors == 3:
                new_board[i, j] = 1
    return new_board

# Função principal para animação
def animate_game(initial_board, iterations=50, interval=500):
    board = initial_board

    # Configura a figura do Matplotlib
    fig, ax = plt.subplots()
    img = ax.imshow(board, cmap='binary', interpolation='nearest')

    def update(frame):
        nonlocal board
        board = update_board(board)
        img.set_data(board)
        return [img]

    # Configura a animação
    ani = FuncAnimation(
        fig, update, frames=iterations, interval=interval, blit=True
    )

    plt.show()

# Tabuleiro inicial
board = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

# Chama a animação
animate_game(board, iterations=100, interval=300)
