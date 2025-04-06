from tabnanny import check


def draw_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def is_full(board):
    # jeśli wszystkie komórki są różne od ' ' zwraca True, jeśli choć jedna jest ' ' to zwraca False
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        draw_board(board)
        try:
            move = int(input(f"Gracz {player}, wybierz pole (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] != ' ':
                print("To pole jest już zajęte, wybierz inne.")
                continue
            board[row][col] = player
        except (ValueError, IndexError):
            print("Niepoprawny ruch, spróbuj ponownie.")
            continue

        if check_winner(board):
            draw_board(board)
            print(f"Gracz {player} wygrywa!")
            break

        if is_full(board):
            draw_board(board)
            print("Remis!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == '__main__':
    tic_tac_toe()

