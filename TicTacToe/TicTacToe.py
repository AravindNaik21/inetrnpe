# Tic Tac Toe

# Create the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    row1 = f' {board[0]} | {board[1]} | {board[2]} '
    row2 = f' {board[3]} | {board[4]} | {board[5]} '
    row3 = f' {board[6]} | {board[7]} | {board[8]} '

    separator = '-' * len(row1)

    print(row1)
    print(separator)
    print(row2)
    print(separator)
    print(row3)

# Function to check if a player has won
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True

    return False

# Function to check if the board is full
def check_draw():
    return ' ' not in board

# Function to make a move
def make_move(player, position):
    board[position] = player

# Main game loop
def play_game():
    current_player = 'X'

    while True:
        print_board()

        position = int(input(f"Player {current_player}, enter your move (0-8): "))

        if board[position] == ' ':
            make_move(current_player, position)

            if check_win(current_player):
                print_board()
                print(f"Player {current_player} wins!")
                break
            elif check_draw():
                print_board()
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

# Start the game
play_game()
