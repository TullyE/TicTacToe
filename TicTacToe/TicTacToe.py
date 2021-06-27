
def display_board(board): 
    
    print('\n'*100)
    #Print the game board
    print(board[7]+'|'+board[8]+'|'+board[9]) 
    print('-|-|-')                            
    print(board[4]+'|'+board[5]+'|'+board[6]) 
    print('-|-|-')                            
    print(board[1]+'|'+board[2]+'|'+board[3]) 
    
    pass
def user_choice():
    # Variables
    PlayerCharacter1 = 'not'     
    acceptable_inputs = 'X', 'O' 
    isxoro = False               
        
        
    while PlayerCharacter1 == 'not' or isxoro == False: 
        
        #Take input from user
        PlayerCharacter1 = input("Player 1 select 'X or 'O': ").upper() 
        
        if PlayerCharacter1 == 'X' or PlayerCharacter1 == 'O': 
            
            isxoro = True
            #return O X or X O
            if PlayerCharacter1 == 'X':
                return ('X', 'O') 
            else:
                return ('O', 'X') 
def win_check(board, mark):
    #Variables
    #index position and while loops exit
    i = 1 
    while i <= 7:
        if board[i] == board[i+1] == board[i+2] == mark: # Rows
             return True
        i += 3 
    i = 1
    while i <= 3:
        if board[i] == board[i+3] == board[i+6] == mark: # Columns
            return True
        i += 1
    if board[1] == board[5] == board[9] == mark: # Bottem left to top right------Diagonal
             return True
    if board[3] == board[5] == board[7] == mark: # Bottem right to top left------Diagonal
             return True
    return False
import random

turn = 1 #Global Var

def choose_first():
    #randomly chooses 1 or 2
    first = random.randint(1,2)
    
    if first == 1:
        turn = 1
    else:
        turn = 2
    return turn #returns either 1 or 2
def space_check(board, position):
    #checks if position is empty
    return board[position] == ' '
def player_choice(board):
    
    #Variables
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position): #persistent asking
        position = int(input('Choose your next position: (1-9) '))
        
    return position #returns an integer
def end_game():
    
    #Has one of the teams won?
    if win_check(Game_board, 'X') == True or win_check(Game_board, 'O') == True: 
        return True
    else:
        return False
print('Welcome to Tic Tac Toe!')

#Variables
Game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' '] #set the Game Board to empty at the start
marker = user_choice() 
display_board(Game_board) 
turn = choose_first() 
lastp = [] 

print(f'Player {turn} was selected to go first!') 

#Logic
while end_game() == False and len(lastp) < 9: #while it's not a win and it's not a tie
    if turn == 1:
        Game_board[player_choice(Game_board)] = marker[0]
        display_board(Game_board)
        lastp.append(1)
        end_game()
        turn += 1

        if end_game()== True or len(lastp) == 9: #if its a win immediately stop
            break
        else: 
            print('Player 2 your turn!')
    if turn == 2:
        Game_board[player_choice(Game_board)] = marker[1]

        display_board(Game_board)
        lastp.append(2)
        end_game()
        turn -= 1

        if end_game()== True or len(lastp) == 9:
            break
        else:
            print('Player 1 your turn!')

if end_game() == True:
    print(f'Player {lastp[-1]}, has won the game!') #if it's a win then the last player who played is the winner
else:
    print('there was a tie')