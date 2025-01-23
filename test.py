'''import pygame
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


# Função principal do jogo
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Test")
    clock = pygame.time.Clock()
    
    while True:
        screen.fill(BLACK)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # Check if the left mouse button is pressed
        left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
        
        # Continue checking while the left mouse button is pressed
        while left_mouse_button_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
            print(left_mouse_button_pressed)
            left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
            print(left_mouse_button_pressed)
        
        print(left_mouse_button_pressed)

        left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
        while left_mouse_button_pressed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            left_mouse_button_pressed = pygame.mouse.get_pressed()[0]
            print(left_mouse_button_pressed)
        print(left_mouse_button_pressed)

        pygame.display.flip()
        clock.tick(FPS)

main()

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
    board = np.zeros((n, n), dtype=int)
    return board

def check_neighbors(board, cell):
    """
    Check the number of live neighbors around a given cell.

    Parameters:
    board (numpy.ndarray): The game board.
    cell (tuple): The coordinates of the cell to check.

    Returns:
    int: The number of live neighbors.
    """
    live_neighbors = 0 
    i = cell[0]
    j = cell[1]

    neighbors = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1), (i, j-1)]
def update_board(prev_board):
    """
    Update the game board to the next state based on the rules of Conway's Game of Life.

    Parameters:
    prev_board (numpy.ndarray): The current state of the game board.

    Returns:
    numpy.ndarray: The next state of the game board.
    """
    board_size = board.shape[0]
    for neighbor in neighbors:
        if neighbor[0] < 0 or neighbor[0] >= board_size or neighbor[1] < 0 or neighbor[1] >= board_size:
            continue
        if board[neighbor] == 1:
            live_neighbors += 1

    return live_neighbors

def update_board(prev_board):
    n = prev_board.shape[0]
    new_board = initialize_board(n)

    for i in range(n):
        for j in range(n):
            alive = prev_board[cell] == 1
            alive = 1 if prev_board[cell] == 1 else 0
            
            live_neighbors = check_neighbors(prev_board, cell)

def handle_events(board, running, CELL_SIZE, offset, panning, pan_start, screen):''''''
    """
    Handle all the events in the game, such as mouse clicks, key presses, and window resizing.

    Parameters:
    board (numpy.ndarray): The game board.
    running (bool): The state of the game (running or paused).
    CELL_SIZE (int): The size of each cell in pixels.
    offset (list): The offset for panning the view.
    panning (bool): Whether the view is currently being panned.
    pan_start (tuple): The starting position of the panning.
    screen (pygame.Surface): The game screen.

    Returns:
    tuple: Updated values for board, running, CELL_SIZE, offset, panning, and pan_start.
    """
 '''               '''new_board[cell] = 1
            elif alive and live_neighbors not in [2, 3]:
                new_board[cell] = 0
            elif not alive and live_neighbors == 3:
                new_board[cell] = 1

    return new_board

def handle_events(board, running, CELL_SIZE, offset, panning, pan_start, screen):
    global panning, pan_start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # left click to activate cell or start panning
                x, y = pygame.mouse.get_pos()
                cell_x, cell_y = (x - offset[0]) // CELL_SIZE, (y - offset[1]) // CELL_SIZE
                if not running:
                    board[cell_y, cell_x] = 1 - board[cell_y, cell_x]
                else:
                    panning = True
                    pan_start = (x, y)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: # stop panning
                panning = False

        if event.type == pygame.MOUSEMOTION:
            if panning:
                x, y = pygame.mouse.get_pos()
                offset[0] += x - pan_start[0]
                offset[1] += y - pan_start[1]
                pan_start = (x, y)
            if panning:
                x, y = pygame.mouse.get_pos()
                offset[0] += x - pan_start[0]
                offset[1] += y - pan_start[1]
                pan_start = (x, y)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and CELL_SIZE <= 60: # scroll up to zoom in
                CELL_SIZE = int(CELL_SIZE * 1.25)
            if event.button == 5 and CELL_SIZE >= 4: # scroll down to zoom out
                CELL_SIZE = int(CELL_SIZE / 1.25)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running 
            if event.key == pygame.K_r:
                board = initialize_board(GRID_SIZE) 
def draw_grid(board, screen, CELL_SIZE, offset):
    
    Draw the game grid on the screen.

    Parameters:
    board (numpy.ndarray): The game board.
    screen (pygame.Surface): The screen to draw on.
    CELL_SIZE (int): The size of each cell in pixels.
    offset (list): The offset for panning the view.
    
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
        global WIDTH, HEIGHT
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            CELL_SIZE = min(WIDTH, HEIGHT) // GRID_SIZE
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
def game_of_life(CELL_SIZE=CELL_SIZE):
    
    Run the Game of Life simulation.

    Parameters:
    CELL_SIZE (int): The size of each cell in pixels.
    
            
    return board, running, int(CELL_SIZE), offset, panning, pan_start

def draw_grid(board, screen, CELL_SIZE, offset):
    screen.fill(BLACK)
        for j in range(GRID_SIZE):  # This line is not needed and can be removed
            pass
def game_of_life(CELL_SIZE=8):
def game_of_life(CELL_SIZE=CELL_SIZE):
    global panning, pan_start
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
    offset = [0, 0]
    panning = False
    pan_start = (0, 0)
        board, running, CELL_SIZE, offset, panning, pan_start = handle_events(board, running, CELL_SIZE, offset, panning, pan_start, screen)
    while True:
        board, running, CELL_SIZE, offset, panning, pan_start = handle_events(board, running, CELL_SIZE, offset, panning, pan_start)

        if running:
            board = update_board(board)

        draw_grid(board, screen, CELL_SIZE, offset)

        pygame.display.flip()
        clock.tick(FPS)

game_of_life()'''

import pygame
import numpy as np
import sys

WIDTH, HEIGHT = 800, 600  
GRID_SIZE = 100            
CELL_SIZE = WIDTH // GRID_SIZE
FPS = 10   
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)


# Função principal
def game_of_life():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Game of Life - Zoom e Arrastar")

    clock = pygame.time.Clock()

    screen.fill(BLACK)

    left_click = pygame.mouse.get_pressed()[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        left_click = pygame.mouse.get_pressed()[0]
        print(left_click)
        
    pygame.display.flip()
    clock.tick(FPS)

# Executar o jogo
if __name__ == "__main__":
    game_of_life()


