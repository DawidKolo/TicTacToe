from IPython.display import clear_output


def player_markers():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, pick X or O: ').upper()

    player_1 = marker

    if player_1 == 'X':
        player_2 = 'O'
    else:
        player_2 = 'X'
    return (player_1, player_2)


def display_board(board):
    clear_output()
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])


board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player_markers()
display_board(board)
