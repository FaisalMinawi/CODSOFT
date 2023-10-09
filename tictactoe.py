import random

# Constants for the board cells
X = 'X'
O = 'O'
EMPTY = ' '

# the Tic-Tac-Toe board
board = [EMPTY] * 9

# Winning combinations
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(' | '.join(row))
        print('---------')

# Function to check if the board is full
def is_board_full(board):
    return EMPTY not in board

# Function to check if the game is over (someone wins or it's a draw)
def is_game_over(board):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != EMPTY:
            return True  # Someone has won
    return is_board_full(board)

# Function to get a list of available moves
def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]

# Function to evaluate the board state for the AI player (Minimax)
def evaluate_board(board):
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == X:
            return 1  # AI (X) wins
        elif board[combo[0]] == board[combo[1]] == board[combo[2]] == O:
            return -1  # Human (O) wins
    return 0  # It's a draw

# Minimax function with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_game_over(board):
        return evaluate_board(board)

    if is_maximizing:
        max_eval = -float('inf')
        for move in available_moves(board):
            board[move] = X
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = O
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move for the AI
def find_best_move(board):
    best_eval = -float('inf')
    best_move = -1
    for move in available_moves(board):
        board[move] = X
        eval = minimax(board, 0, False, -float('inf'), float('inf'))
        board[move] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Main game loop
while not is_game_over(board):
    print_board(board)
    while True:
        try:
            human_move = int(input("Enter your move (1-9): "))
            if human_move in range(1, 10) and board[human_move - 1] == EMPTY:
                board[human_move - 1] = O
                break
            else:
                print("Invalid input or cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")


    if is_game_over(board):
        break

    ai_move = find_best_move(board)
    board[ai_move] = X

print_board(board)

if evaluate_board(board) == 1:
    print("AI wins!")
elif evaluate_board(board) == -1:
    print("Human wins!")
else:
    print("It's a draw!")
