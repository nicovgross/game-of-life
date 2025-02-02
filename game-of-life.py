import numpy as np
import sys
import pygame

WIDTH, HEIGHT = 800, 600  
GRID_SIZE = 100            
CELL_SIZE = WIDTH // GRID_SIZE       
        
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

def count_population(board):
    return np.sum(board)

def handle_events(board, running, iteration, generations, CELL_SIZE, offset, state, grid, FPS):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  #left click to activate cell or drag the grid
                state["dragging"] = True
                state["initial_position"] = pygame.mouse.get_pos()
                state["moved"] = False  #flag to check if there was a significant movement

            if event.button == 4 and CELL_SIZE <= 60: #scroll up to zoom in
                    CELL_SIZE = int(CELL_SIZE * 1.25)
            if event.button == 5 and CELL_SIZE >= 6: #scroll down to zoom out
                    CELL_SIZE = int(CELL_SIZE / 1.25)

        #detects if user is dragging the grid
        if event.type == pygame.MOUSEMOTION and state["dragging"]:
            current_mouse_pos = pygame.mouse.get_pos()
            dx = current_mouse_pos[0] - state["initial_position"][0]
            dy = current_mouse_pos[1] - state["initial_position"][1]

            if abs(dx) > 3 or abs(dy) > 3:  #defines whether the movement was significant enough
                offset[0] += dx
                offset[1] += dy
                state["initial_position"] = current_mouse_pos  #updates initial position
                state["moved"] = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  #left click to activate cell
                state["dragging"] = False

                #only activates cell if there was no significant movement
                if not state["moved"]:
                    x, y = pygame.mouse.get_pos()
                    cell_x, cell_y = (x - offset[0]) // CELL_SIZE, (y - offset[1]) // CELL_SIZE
                    if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                        board[cell_y, cell_x] = 1 - board[cell_y, cell_x]

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
            if event.key == pygame.K_r:
                board = initialize_board(GRID_SIZE)
                iteration = 0
                generations = [board]
                running = False
            if event.key == pygame.K_f:
                pygame.display.toggle_fullscreen()
            if event.key == pygame.K_g:
                grid = not grid
            if event.key == pygame.K_UP and FPS < 60:  #increase FPS
                FPS += 1
            if event.key == pygame.K_DOWN and FPS > 1:  #decrease FPS
                FPS -= 1
            if event.key == pygame.K_LEFT and iteration > 0 and not running:  #go back one generation
                iteration -= 1
                board = generations[iteration]
            if event.key == pygame.K_RIGHT and not running:  #go forward one generation
                iteration += 1
                board = update_board(board)
                generations.append(board)

    return board, running, iteration, generations, CELL_SIZE, offset, grid, FPS

def draw_grid(board, screen, CELL_SIZE, offset, grid):
    screen.fill(BLACK)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(j * CELL_SIZE + offset[0], i * CELL_SIZE + offset[1], CELL_SIZE, CELL_SIZE)
            color = WHITE if board[i, j] == 1 else BLACK
            pygame.draw.rect(screen, color, rect)
            if grid:
                pygame.draw.rect(screen, GRAY, rect, 1)

def game_of_life(CELL_SIZE=CELL_SIZE):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    pygame.font.init() 
    
    FPS = 10  #frames per second
    font = pygame.font.SysFont("Arial", 20, bold=True)
    board = initialize_board(GRID_SIZE)
    generations = [board]
    iteration = 0
    population = 0 #number of live cells
    running = False  
    offset = [0, 0] #indicates how far the grid has been dragged, and used to display the grid in the correct position
    grid = True  #flag to display grid

    #dictionary that handles mouse dragging
    state = {"dragging": False, "initial_position": None}

    pause_icon = pygame.image.load(r"img/Pause_icon.png")
    unpause_icon = pygame.image.load(r"img/Unpause_icon.png")
    pause_icon_scaled = pygame.transform.scale(pause_icon, (50, 50))
    unpause_icon_scaled = pygame.transform.scale(unpause_icon, (50, 50))

    while True:
        FPS_text = font.render(f"FPS: {FPS}", True, (84, 84, 84))
        iteration_text = font.render(f"Iteration: {iteration}", True, (84, 84, 84))
        population_text = font.render(f"Population: {population}", True, (84, 84, 84))

        board, running, iteration, generations, CELL_SIZE, offset, grid, FPS = handle_events(board, running, iteration, generations, CELL_SIZE, offset, state, grid, FPS)
        population = int(np.sum(board))

        draw_grid(board, screen, CELL_SIZE, offset, grid)

        screen.blit(FPS_text, (10, 70))
        screen.blit(iteration_text, (10, 100))
        screen.blit(population_text, (10, 130))

        if running:
            board = update_board(board)
            iteration += 1
            generations.append(board)
            unpause_icon_scaled.set_alpha(150)
            screen.blit(unpause_icon_scaled, (10, 10))
        else:
            pause_icon_scaled.set_alpha(150)
            screen.blit(pause_icon_scaled, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_of_life()