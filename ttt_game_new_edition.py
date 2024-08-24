# Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def player_turn(board, player):
    while True:
        try:
            row = int(input(f"Enter the row (1-3) where you'd like to place your '{player}': ")) - 1
            col = int(input(f"Enter the column (1-3) where you'd like to place your '{player}': ")) - 1
            if 0 <= row < 3 and 0 <= col < 3 and make_move(board, row, col, player):
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number within the board's range.")

def minimax(board, depth, is_maximizing, player):
    if player == "X":
        opponent = "O"
    else:
        opponent = "X"

    if check_win(board, player):
        return 1
    elif check_win(board, opponent):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == " ":
                    board[row][col] = player
                    score = minimax(board, depth + 1, False, player)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == " ":
                    board[row][col] = opponent
                    score = minimax(board, depth + 1, True, player)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score


def computer_turn(board, player):
    print("Computer's turn:")
    best_score = float('-inf')
    move = (None, None)
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == " ":
                board[row][col] = player
                score = minimax(board, 0, False, player)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    make_move(board, *move, player)

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