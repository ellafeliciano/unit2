'''
#################
Lab 2.06
#################
1. In your Notebook
-------------------
Predict what will be printed then type the program in your console to confirm
Example 1
    a = 0
    while a < 10:
        print(a)

prediction: 0
actual: 0

Example 2
    a = 0
    while a < 10:
        a = a + 1
        print(a)

prediction: 12345678910
actual: 12345678910

2. In your Notebook
-------------------
Create a set of test cases for the following sample code and predict the behavior
    a = input("Would you like to quit: ")
    while a != "y" and a != "n" :
        a = input("Would you like to quit: ")

test cases: 'y', 'n', 'q', 'cat'

a = input("Would you like to quit: ")
while a != "y" and a != "n" and a != "q" and a != "cat" :
        a = input("Would you like to quit: ")

3. Implement the Tic Tac Toe game using a while loop
----------------------------------------------------
Allow users to keep playing (max 9 times).

Use variables to decide whose turn it is, and greet them as Xs or Os.

User picks a location on the board according to the number:
        1 | 2 | 3
        ---------
        4 | 5 | 6
        ---------
        7 | 8 | 9


Depending on the position user gave, update the corresponding position of the board to reflect that.

Print the updated board out.

You will not need to determine the winner at this point.
(Copy and paste your previous tic-tac-toe version and modify the code to implement the above)
'''
# Basic Tic-Tac-Toe game

# initial variables
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
turns = 0 
player = 1 # keep track of whose turn it is
player_symbol = ""

# print starting board 
print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
print("---------")
print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
print("---------")
print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
print()

# main game loop
while turns < 9:
    if player == 1:
        player_symbol = 'X'
    else:
        player_symbol = 'O'
    player_choice = int(input(f"Choose a number to place your {player_symbol} "))

    # locate where to place symbol
    if player_choice == 1:
        board[0][0] = player_symbol
    elif player_choice == 2:
        board[0][1] = player_symbol
    elif player_choice == 3:
        board[0][2] = player_symbol
    elif player_choice == 4:
        board[1][0] = player_symbol
    elif player_choice == 5:
        board[1][1] = player_symbol
    elif player_choice == 6:
        board[1][2] = player_symbol
    elif player_choice == 7:
        board[2][0] = player_symbol
    elif player_choice == 8:
        board[2][1] = player_symbol
    elif player_choice == 9:
        board[2][2] = player_symbol
    else:
        print("invalid choice")

    turns += 1

    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print()

    # determine next player 
    if player == 1:
        player = 2
    else:
        player = 1
print("Game over")


    
