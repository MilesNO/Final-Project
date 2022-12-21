print("""Wecome to TicTacToe
  _   _   _
| _ | _ | _ |
| _ | _ | _ |
| _ | _ | _ |""")


#Steps
#We first make a game board
#Collect player's input
#Check row, column and diagonals for 
import random
board= ['_','_','_','_','_','_','_','_','_']
player = 'X'
winner= ' '


print('\n')
#creates game board
def gameboard(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")


#collects player input
#1-9 represents the spaces on the board
def playerinput(board):
    player_input=int(input("Enter a number from 1-9: "))
    if player_input >= 1 and player_input <= 9 and board[player_input-1] == '_':
        board[player_input-1] = player
    else:
        print("spot is taken")

def checkboardrow(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != '_':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '_':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '_':
        winner = board[6]
        return True

def checkboardcolumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '_':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '_':
        winner = board[3]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '_':
        winner = board[2]
        return True

def checkdiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != '_':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        winner = board[2]
        return True

def Tie():
    if '_' not in board:
        gameboard(board)
        print('It\'s a tie')

def win():
    if checkboardcolumn(board) or checkboardrow(board) or checkdiagonal(board):
        print(f'The winner is {player}')

def playerswitch():
    global player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

#To play against the computer
#def computerplayer(board):
#    import random
#    while player == "O":
#        spot= random.randint(0,8)
#        if board[spot] == "_":
#            board[spot] = "O"
#            playerswitch()
            

while True:
    gameboard(board)
    playerinput(board)
    win()
    Tie()
    playerswitch()
    #computerplayer(board)
    #win()
    #Tie()
    
    

