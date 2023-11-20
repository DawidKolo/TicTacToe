from IPython.display import clear_output

board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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

def marker_placing(board, marker, position):

    board[position] = marker

def players_move():
    position = 0

    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Please select a position of your marker [1-9]: ')

    return int(position)







#player_markers()

#marker_placing(board, 'o', 2)
#display_board(board)
players_move()
