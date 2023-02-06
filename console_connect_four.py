from collections import deque


class FullColumnError(Exception):
    pass


def player_count():

    while True:
        try:
            players_amount = int(input('Please choose the amount of players.\n'))

            if players_amount < 1:
                raise ValueError

        except ValueError:
            print(ValueError('Player count should be a positive number.'))

        else:
            break

    return deque([n, 0] for n in range(1, players_amount + 1))


def directions_search(row_len, col_len, board, current_spot, player_info):
    row_i, col_i = current_spot

    left = [board[row_i][i] for i in range(col_i, -1, -1)]

    left_up = [board[row_i - i][col_i - i] for i in range(4)
               if row_i - i in range(row_len) and col_i - i in range(col_len)]

    up = [board[i][col_i] for i in range(row_i, -1, -1)][:4]

    up_right = [board[row_i - i][col_i + i] for i in range(4)
                if row_i - i in range(row_len) and col_i + i in range(col_len)]

    right = [board[row_i][i] for i in range(col_i, col_len)][:4]

    down_right = [board[row_i + i][col_i + i] for i in range(4)
                  if row_i + i in range(row_len) and col_i + i in range(col_len)]

    down = [board[i][col_i] for i in range(row_i, row_len)][:4]

    down_left = [board[row_i + i][col_i - i] for i in range(4)
                 if row_i + i in range(row_len) and col_i - i in range(col_len)]

    return 4 * [player_info] in (
            left, left_up, up, up_right,
            right, down_right, down, down_left
    )


def check_if_won(player_moves_counter, rows_len, columns_len, board, current_spot, player_info):

    return player_moves_counter >= 4 and directions_search(rows_len, columns_len, board, current_spot, player_info)


rows, columns = 6, 7
board_matrix = [[0] * 7 for _ in range(6)]
spots_n = 6 * 7
players = player_count()
winner = False

[print(row) for row in board_matrix]
while spots_n and not winner:

    current_player = players[0][0]

    try:
        column_choice = int(input(f'Player {current_player}, please choose a column.\n')) - 1

        if column_choice < 0:
            raise IndexError

        column = [board_matrix[current_row][column_choice] for current_row in range(rows)]

        if 0 in column:
            row_column = rows - 1 - column[::-1].index(0)
            board_matrix[row_column][column_choice] = current_player
            players[0][1] += 1
            spots_n -= 1

            if check_if_won(players[0][1], rows, columns, board_matrix, [row_column, column_choice], current_player):
                winner = current_player
        else:
            raise FullColumnError

    except (IndexError, ValueError):
        print('Column choice must be a number from 1 to 7.')

        continue

    except FullColumnError:
        # noinspection PyUnboundLocalVariable
        print(FullColumnError(f'Column {column_choice + 1} is full. Please choose another.'))

        continue

    [print(row) for row in board_matrix]

    players.rotate(-1)

if winner:
    print(f'Player {winner} won!')
else:
    print('Draw! Board is full.')
