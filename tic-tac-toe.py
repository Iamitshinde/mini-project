# Tic-Tac-Toe game in Python

# Display the board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Check for a winner
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if the board is full (tie)
def is_full(board):
    return all(cell != " " for cell in board)

# Main game loop
def play_game():
    board = [" "] * 9  # 9 empty cells
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if board[move] != " ":
                print("That spot is already taken. Try again!")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Choose a number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player
        print_board(board)

        # Check winner
        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check tie
        if is_full(board):
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
