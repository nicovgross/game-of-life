'''import pygame

# pygame setup
pygame.init()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

def draw_grid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_WIDTH, WINDOW_HEIGHT):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    draw_grid()

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()'''

import pygame
import numpy as np
import sys

# Configurações do jogo
WIDTH, HEIGHT = 800, 600  # Tamanho da janela
GRID_SIZE = 50            # Quantidade de células por lado (GRID_SIZE x GRID_SIZE)
CELL_SIZE = WIDTH // GRID_SIZE  # Tamanho de cada célula em pixels
FPS = 4                  # Quadros por segundo

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Inicializa o tabuleiro
def initialize_board(grid_size):
    return np.zeros((grid_size, grid_size), dtype=int)

# Atualiza o tabuleiro com base nas regras
def update_board(board):
    new_board = board.copy()
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            live_neighbors = sum(
                board[x % board.shape[0], y % board.shape[1]]
                for x in (i-1, i, i+1)
                for y in (j-1, j, j+1)
                if (x, y) != (i, j)
            )
            if board[i, j] == 1 and live_neighbors not in [2, 3]:
                new_board[i, j] = 0
            elif board[i, j] == 0 and live_neighbors == 3:
                new_board[i, j] = 1
    return new_board

# Função principal do jogo
def game_of_life():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    board = initialize_board(GRID_SIZE)
    running = False  # Controla o estado do jogo
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not running:
                # Ativar/Desativar células com o clique do mouse
                x, y = pygame.mouse.get_pos()
                cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
                board[cell_y, cell_x] = 1 - board[cell_y, cell_x]  # Alterna entre 0 e 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running  # Iniciar/Parar o jogo
                if event.key == pygame.K_r:
                    board = initialize_board(GRID_SIZE)  # Reinicia o tabuleiro
                    running = not running

        # Atualiza o tabuleiro se o jogo estiver em execução
        if running:
            board = update_board(board)

        # Desenha o grid e as células
        screen.fill(BLACK)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = WHITE if board[i, j] == 1 else BLACK
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, GRAY, rect, 1)

        pygame.display.flip()
        clock.tick(FPS)

# Executa o jogo
if __name__ == "__main__":
    game_of_life()
