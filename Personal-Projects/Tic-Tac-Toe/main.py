from IPython.display import clear_output
import time
import random

def display_board(board):

    clear_output()
    
    print('      |      |      ')
    print('  {}   |  {}   |  {}   '.format(board[1],board[2],board[3],))
    print('______|______|______')
    print('      |      |      ')
    print('  {}   |  {}   |  {}   '.format(board[4],board[5],board[6],))
    print('______|______|______')
    print('      |      |      ')
    print('  {}   |  {}   |  {}   '.format(board[7],board[8],board[9],))
    print('      |      |      ')





def player_input():
    
    marker = ''
    while marker != 'X' and marker != 'O' and marker != 'x' and marker != 'o' and marker != '0':
        marker = input('PLAYER1: Enter X or O: ')
        if marker != 'X' and marker != 'O' and marker != 'x' and marker != 'o' and marker != '0':
            print('That is not X or O')

    if marker == '0':
        marker = 'O'
        
    if marker.upper() == 'X':
        return ('X','O')
    elif marker.upper() == 'O':
        return ('O','X')





def place_marker(board, marker, position):
    
    board[position] = marker





def win_check(board, mark):
    
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or #Line 1
    (board[4] == mark and board[5] == mark and board[6] == mark) or #Line 2
    (board[7] == mark and board[8] == mark and board[9] == mark) or #Line 3
    (board[1] == mark and board[4] == mark and board[7] == mark) or #Column 1
    (board[2] == mark and board[5] == mark and board[8] == mark) or #Column 2
    (board[3] == mark and board[6] == mark and board[9] == mark) or #Column 3
    (board[1] == mark and board[5] == mark and board[9] == mark) or #Diagonal 1
    (board[3] == mark and board[5] == mark and board[7] == mark)) #Diagonal 2





def choose_first():
    
    random_num_start = random.randint(0,1)
    
    if random_num_start == 0:
        return 'PLAYER1'
    else:
        return 'PLAYER2'





def space_check(board, position):
    
    return board[position] == ' '





def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True





def player_choice(board, player, marker):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input(f'{player} ({marker}): Choose your position (1-9): '))
    
    return position





def replay():
    
    play_again = input('Do you want to play again? (Yes or No): ')
    
    return play_again.lower() == 'yes'










def game_setup():
    
    
    global the_board
    global game_on
    global turn
    global player1_marker
    global player2_marker
    
    the_board = [' ']*10
    start_game = input('Ready to play? (Yes or No): ')
    time.sleep(0.5)
    
    if start_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False
        return True
        
    player1_marker,player2_marker = player_input()
    time.sleep(1)
    
    turn = choose_first()
    clear_output()
    time.sleep(0.5)
    
    if turn == 'PLAYER1':
        player_starts_marker = player1_marker
    elif turn == 'PLAYER2':
        player_starts_marker = player2_marker
        
    print(f'{turn} ({player_starts_marker}) starts')
    time.sleep(3)









def player1_turn():
    
    global the_board
    global game_on
    global turn
    global position
    
    display_board(the_board)
    time.sleep(0.5)
            
    position = player_choice(the_board,turn,player1_marker)
    place_marker(the_board,player1_marker,position)
    time.sleep(0.25)
            
    if win_check(the_board,player1_marker):
        display_board(the_board)
        time.sleep(0.5)
                
        print(f'PLAYER1 ({player1_marker}) wins!!!')
        time.sleep(4)
                
        game_on = False

    elif full_board_check(the_board):
        display_board(the_board)
        time.sleep(0.5)
                
        print("It's a tie!")
        time.sleep(4)
                
        game_on = False
    else:
        turn = 'PLAYER2'









def player2_turn():
    
    global the_board
    global game_on
    global turn
    global position
    
    display_board(the_board)
    time.sleep(0.5)
            
    position = player_choice(the_board,turn,player2_marker)
    place_marker(the_board,player2_marker,position)
    time.sleep(0.25)
            
    if win_check(the_board,player2_marker):
        display_board(the_board)
        time.sleep(0.5)
                
        print(f'PLAYER2 ({player2_marker}) wins!!!')
        time.sleep(4)
                
        game_on = False
                
    elif full_board_check(the_board):
        display_board(the_board)
        time.sleep(0.5)
                
        print("It's a tie!")
        time.sleep(4)
                
        game_on = False
    else:
        turn = 'PLAYER1'









def end_of_game():
    if not replay():
        time.sleep(1.5)
        
        return True
        
    time.sleep(1.5)
    
    clear_output()
    time.sleep(2)



















print('Welcome to Tic Tac Toe!')
time.sleep(1)

while True:
    
    if game_setup():
        break
    
    while game_on:

        
        if turn == 'PLAYER1':
            
            player1_turn()
            
        
        elif turn == 'PLAYER2':
            
            player2_turn()
        
        
    if end_of_game():
        break
