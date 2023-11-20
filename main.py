from IPython.display import clear_output
# board list
board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# choosing if player is X or O
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

# displaying the game board
def display_board(board):
    clear_output()
    print('')
    print('')
    print('   |   |   ')
    print(' '+board[1]+' ' + '|'+' ' + board[2] + ' '+'|'+' ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' ' + '|'+' ' + board[5] + ' '+'|'+' ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[7]+' ' + '|'+' ' + board[8] + ' '+'|'+' ' + board[9])
    print('   |   |   ')
    print('')
    print('')

#
def marker_placing(board, marker, position):

    board[position] = marker
#taking players input
def players_move():
    position = 0

    while position not in ['1','2','3','4','5','6','7','8','9'] or space_check(board, position):
        position = input('Please select a position of your marker [1-9]: ')

    return int(position)
# check if the space is available
def space_check(board, position):
    return board[position] == 'O' or board[position] == 'X'



#####################################################################
#testing area

#player_markers()

marker_placing(board, 'O', 2)
print(space_check(board, 2))
display_board(board)
#print(board)
#players_move()

