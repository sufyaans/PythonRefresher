#Simple guess the number game
import random


def numberGuess():
    user_guess = int(input("Guess a number: "))
    correct = random.randint(1,10)
    i = 0

    while user_guess != correct:
        print("Try again")
        i += 1
        if correct % 2 == 0:
            print("Hint: The number is even")
        
        else:
            print("Hint: The number is odd")

        print("Number of Guesses: " + str(i))
        user_guess = int(input("Guess a number: "))


    print("You got it")

numberGuess()