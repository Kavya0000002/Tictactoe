def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)
    players = ['X', 'O']
    player_idx = 0

    while True:
        print_board(board)
        player = players[player_idx]
        print(f"Player {player}'s turn")

        row = int(input("Enter the row (0, 1, 2): ")
        col = int(input("Enter the column (0, 1, 2): ")

        if board[row][col] == ' ':
            board[row][col] = player
            if check_win(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player_idx = 1 - player_idx
        else:
            print("That cell is already taken. Try again.")

if __name__ == "__main__":
    main()
