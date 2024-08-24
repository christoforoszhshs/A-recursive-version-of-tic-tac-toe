def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)


def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def check_win(board, player, row=0, col=0, direction=None):
    if row >= len(board) or col >= len(board[0]):
        return False
    if direction is None:
        # Check all directions from the first move
        return (check_win(board, player, row, 0, 'H') or
                check_win(board, player, 0, col, 'V') or
                check_win(board, player, 0, 0, 'D') or
                check_win(board, player, 0, len(board[0])-1, 'AD'))
    elif direction == 'H':
        return board[row][col] == player and (col == len(board[0])-1 or check_win(board, player, row, col+1, 'H'))
    elif direction == 'V':
        return board[row][col] == player and (row == len(board)-1 or check_win(board, player, row+1, col, 'V'))
    elif direction == 'D':
        return board[row][col] == player and (row == len(board)-1 or check_win(board, player, row+1, col+1, 'D'))
    elif direction == 'AD':
        return board[row][col] == player and (row == len(board)-1 or check_win(board, player, row+1, col-1, 'AD'))


def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


def player_turn(board, player):
    while True:
        try:
            row = int(input(f"Enter the row (1-{len(board)}) where you'd like to place your '{player}': ")) - 1
            col = int(input(f"Enter the column (1-{len(board[0])}) where you'd like to place your '{player}': ")) - 1
            if make_move(board, row, col, player):
                break
            else:
                print("That spot is taken. Try another.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number within the board's range.")


def computer_turn(board, player):
    print("Computer's turn:")
    # For simplicity, the computer makes random moves. 
    # A recursive algorithm for the perfect game can be very complex.
    import random
    while True:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)
        if make_move(board, row, col, player):
            break


def switch_player(player):
    return 'O' if player == 'X' else 'X'


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            player_turn(board, current_player)
        else:
            computer_turn(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player '{current_player}' wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    main()
