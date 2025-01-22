import numpy as np
import sys
import pygame

WIDTH, HEIGHT = 800, 600  
GRID_SIZE = 100            
CELL_SIZE = WIDTH // GRID_SIZE  
FPS = 10         
        
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

def initialize_board(n):
    board = np.zeros([n, n])
    return board

def check_neighbors(board, cell):
    live_neighbors = 0 
    i = cell[0]
    j = cell[1]

    neighbors = [tuple([i-1, j-1]), tuple([i-1, j]), tuple([i-1, j+1]), tuple([i, j+1]),
                 tuple([i+1, j+1]), tuple([i+1, j]), tuple([i+1, j-1]), tuple([i, j-1])]
    
    for neighbor in neighbors:
        if neighbor[0] < 0 or neighbor[0] > board.shape[0]-1 or neighbor[1] < 0 or neighbor[1] > board.shape[0]-1:
            continue
        if board[neighbor] == 1:
            live_neighbors += 1

    return live_neighbors

def update_board(prev_board):
    n = prev_board.shape[0]
    new_board = initialize_board(n)

    for i in range(n):
        for j in range(n):
            cell = tuple([i, j])
            alive = 1 if prev_board[cell] == 1 else 0
            
            live_neighbors = check_neighbors(prev_board, cell)

            if alive and live_neighbors in [2, 3]:
                new_board[cell] = 1
            elif alive and live_neighbors not in [2, 3]:
                new_board[cell] = 0
            elif not alive and live_neighbors == 3:
                new_board[cell] = 1

    return new_board

def handle_events(board, running, CELL_SIZE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not running:
            if event.button == 1: #left click to activate cell
                x, y = pygame.mouse.get_pos()
                cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
                board[cell_y, cell_x] = 1 - board[cell_y, cell_x]
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and CELL_SIZE <= 60: #scroll up to zoom in
                    CELL_SIZE *= 1.25
            if event.button == 5 and CELL_SIZE >= 4: #scroll down to zoom out
                    CELL_SIZE //= 1.25
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running 
            if event.key == pygame.K_r:
                board = initialize_board(GRID_SIZE) 
                running = False
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            
    return board, running, int(CELL_SIZE)

def draw_grid(board, screen, CELL_SIZE):
    screen.fill(BLACK)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE if board[i, j] == 1 else BLACK
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def game_of_life(CELL_SIZE=CELL_SIZE):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    board = initialize_board(GRID_SIZE)
    running = False  
    while True:
        board, running, CELL_SIZE = handle_events(board, running, CELL_SIZE)

        if running:
            board = update_board(board)

        draw_grid(board, screen, CELL_SIZE)

        pygame.display.flip()
        clock.tick(FPS)

game_of_life()