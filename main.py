import random


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
    #    print('\n' * 100)

    print('')
    print('')
    print('   |   |   ')
    print(' ' + board[1] + ' ' + '|' + ' ' + board[2] + ' ' + '|' + ' ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' ' + '|' + ' ' + board[5] + ' ' + '|' + ' ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' ' + '|' + ' ' + board[8] + ' ' + '|' + ' ' + board[9])
    print('   |   |   ')
    print('')
    print('')


#
def marker_placing(board, marker, position):
    board[position] = marker


# taking players input
def players_move(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or space_check(board, position):
        temp = input('Please select a position of your marker [1-9]: ')
        position = int(temp)
    return position


# check if the space is available
def space_check(board, position):
    return board[position] == 'O' or board[position] == 'X'


def full_board(board):
    for i in range(1, 10):
        if not space_check(board, i):
            return False
    return True


def winner_chck(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))


def player_draw():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def keep_playing():
    return input('Would you like to play once again? [y/n] ').lower().startswith('y')


print('Welcome to Tic Tac Toe')

pl1 = input('What is the name of the player 1? ')
pl2 = input('What is the name of the player 2? ')

while True:
    # board list
    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    pl1_mark, pl2_mark = player_markers()

    turn = player_draw()
    print(turn + ' will play first.')

    while True:
        if turn == 'Player 1':
            display_board(board)
            position = players_move(board)
            marker_placing(board, pl1_mark, position)

            if winner_chck(board, pl1_mark):
                display_board(board)
                print('Congrats, ' + f'{pl1} ' + 'has won!!!')
                break
            else:
                if full_board(board):
                    display_board(board)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            position = players_move(board)
            marker_placing(board, pl2_mark, position)

            if winner_chck(board, pl2_mark):
                display_board(board)
                print('Congrats, ' + f'{pl2} ' + 'has won!!!')
                break
            else:
                if full_board(board):
                    display_board(board)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player 1'
    if not keep_playing():
        break
