# File : CS112_A1_T2_Game1_20230063.py.
# Purpose : the first who reaches number 100 wins
# Author : Ismail Mostafa Ali
# ID : 20230063

# Define a function for the main game
def the_game():
    sum = 0  # Set the sum variable to zero
    print("welcome to hundred game")  # show a welcome message for the game
    print("get hundred to win")

    while sum < 100:  # Making a while loop
        move = int(input("player 1 choose number from 1 to 10 : "))  # Let player 1 enter a number
        while move < 1 or move > 10:  # Check the entered number is between 1 and 10
            move = int(input("player 1 choose number from 1 to 10 : "))
        sum += move  # Add the entered number to the variable sum
        print('now we have ', sum)  # Showing the sum we have now
        if sum >= 100:  # Check if the sum reach 100
            print("player 1 is the winner ")  # If player 1 reach 100 show this message
            break

        move = int(input("player 2 choose number from 1 to 10 : "))  # Let player 2 enter a number
        while move < 1 or move > 10:  # Making a while loop if the move less than 1 or more than 10
            move = int(input("player 1 choose number from 1 to 10 : "))  # Let player 1 enter a number
        sum += move  # Add the entered number to the sum
        print('now we have ', sum)  # Showing the sum we have now
        if sum >= 100:  # Check if the sum more than 100
            print("player 2 is the winner")  # If the sum more than 100 show this message
            break


the_game()
