import random


def display_board(board):
        # prints the board, with all the positions of the input list
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3] + '\100n')


def player_input():
        # takes in the markers for each player
    marker = 'A'
    while marker != 'X' and marker != "O":
        marker = (input('player1 Choose X or O: ')).upper()
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
            print(f'player1:X \n player2:O')
        elif player1 == 'O':
            player2 = 'X'
            print(f' player1:O\nplayer2:X')
    return (player1, player2)
    # the exit is a tuple, which can later be used via tuple


def place_marker(board, marker, position):
        # takes in the board list object, a marker a
        # and a desired position and assigns it to the board
    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            # across the top
            # across the middle
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            # across the bottom
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            # down the middle
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            # down the right side
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            # diagonal
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
        # random choice of who plays first
    if random.randint(0, 1) == 0:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):

        # Write a function that checks if the board is full
        # and returns a boolean value
        # True if full, False otherwise.
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
        # Write a function that asks for a player's next position
        # (as a number 1-9) and then uses
        # the function from step 6 to check if it's a free position.
        # If it is, then return the position for later use.
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')



print('Welcome to Tic Tac Toe!')



# used to print the initial positions o
# n the board
print("Board Positions\n")



# used to display the positions of the board at the start of the game
test_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
display_board(test_board)

# tuple unpacking to make use od the players chosen markers in the function


while True:
        # actual game board
    game_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'Will go first')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display_board(game_board)
            print('player1')
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)
            if win_check(game_board, player1_marker):
                display_board(game_board)
                game_on != False
                print('Game over')
                break
            else:
                if full_board_check(game_board):
                    print('The game is a draw')
                    break
                else:
                    turn = 'player2'
        else:
            display_board(game_board)
            print('player2')
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)
            if win_check(game_board, player2_marker):
                display_board(game_board)
                game_on != False
                print('Game over')
                break
            else:
                if full_board_check(game_board):
                    print('The game is a draw')
                    break
                else:
                    turn = 'player1'
    if not replay():
        break