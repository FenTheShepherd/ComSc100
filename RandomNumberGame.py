# we need the random "library"
from random import randrange

# makes a number between 0 and 100 (excluding 100)
# and it saves it into a variable called "answer"
answer = randrange(100)

# Run the code inside of the While loop forever
while True:
    # ask the player for a number and save it
    player_guess = int(input("Please Guess a Number: "))
    if answer == player_guess:
        print('You Win!')
        break #end the game by breaking the loop
    if (answer < player_guess):
        print("It's smaller!")
    else: print("It's Bigger!")