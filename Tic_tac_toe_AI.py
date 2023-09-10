import random

# Initialize the Tic Tac Toe board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the board is full
def is_board_full(board):
    return ' ' not in board

# Function to check if someone has won
def check_win(board, player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function for the AI to make a random move
def ai_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(empty_cells)

# Main game loop
while True:
    print_board(board)
    
    # Player's move
    player_move = int(input("Enter your move (1-9): ")) - 1
    
    if board[player_move] == ' ':
        board[player_move] = 'X'
    else:
        print("Invalid move. Try again.")
        continue
    
    # Check if the player has won
    if check_win(board, 'X'):
        print_board(board)
        print("Congratulations! You win!")
        break
    
    # Check if the board is full (tie)
    if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        break
    
    # AI's move
    ai_move_index = ai_move(board)
    board[ai_move_index] = 'O'
    
    # Check if the AI has won
    if check_win(board, 'O'):
        print_board(board)
        print("AI wins! You lose.")
        break
