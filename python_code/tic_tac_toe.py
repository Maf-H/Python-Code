from random import randint
plus = '+'*4
dash = '-'*7
bar = '|'
n = [1,2,3,4,5,6,7,8,9]
def display_board(n):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(dash.join(plus))
    for i in range(3):
        print(f'|       |       |       |')
        if i == 0:
            print(f'|   {n[i]}   |   {n[i + 1]}   |   {n[i + 2]}   |')
        elif i == 1:
            print(f'|   {n[i*2 + 1]}   |   {n[i*2 + 2]}   |   {n[i*2 + 3]}   |')
        else:
            print(f'|   {n[i*2 + 2]}   |   {n[i*2 + 3]}   |   {n[i*2 + 4]}   |')
        print(f'|       |       |       |')
        print(dash.join(plus))
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    comp_input = int(randint(1,9))
    while board[comp_input-1] =='X' or board[comp_input-1] =='O':
        comp_input = int(randint(1,9))
    board[comp_input-1] = 'O'
    display_board(board)
    user_input = input("Enter your move: ")
    board[user_input - 1] = 'O'
    display_board(board)
# TODO
def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass

def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass

