import numpy as np

def initialize_board(n):
    board = np.zeros([n, n])
    return board

def check_neighbors(board, cell):
    live_neighbors = 0 
    i = cell[0]
    j = cell[1]

    neighbors = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j+1],
                 [i+1, j+1], [i+1, j], [i+1, j-1], [i, j-1]]
    
    for neighbor in neighbors:
        if neighbor[0] < board.shape[0] or neighbor[0] > board.shape[0] or neighbor[1] < board.shape[0] or neighbor[1] > board.shape[0]:
            break
        print(neighbor)
        if board[neighbor] == 1:
            live_neighbors += 1

    '''if board[i-1, j-1] == 1:
        live_neighbors += 1
    elif board[i-1, j] == 1:
        live_neighbors += 1
    elif board[i-1, j+1] == 1:
        live_neighbors += 1
    elif board[i, j+1] == 1:
        live_neighbors += 1
    elif board[i+1, j+1] == 1:
        live_neighbors += 1
    elif board[i+1, j] == 1:
        live_neighbors += 1
    elif board[i+1, j-1] == 1:
        live_neighbors += 1
    elif board[i, j-1] == 1:
        live_neighbors += 1 '''

    return live_neighbors

def update_board(prev_board):
    n = prev_board.shape[0]
    new_board = initialize_board(n)

    for i in range(n):
        for j in range(n):
            cell = tuple([i, j])

            alive = 0
            if prev_board[cell] == 1:
                alive = 1
            
            live_neighbors = check_neighbors(prev_board, cell)
            print(live_neighbors)

            if alive and live_neighbors < 2:
                new_board[cell] = 0
            elif alive and live_neighbors in range(2, 3):
                new_board[cell] = 1
            elif alive and live_neighbors > 3:
                new_board[cell] = 0
            elif not alive and live_neighbors == 3:
                new_board[cell] = 1

    return new_board

def main(initial_board):
    board = initial_board

    i=0
    while True:
        if i == 10:
            break
        print(board)
        print("\n")
        board = update_board(board)

        i+=1

board = np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]])

main(board)
