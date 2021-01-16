# Program picks a number between 1-10 and user has 3 attempts to guess number

import random

number = random.randint(1, 10)

for i in range(3):
    guess = int(input("What is the number: "))
    if guess > number:
        print("Try a little lower!")
    elif guess < number:
        print("Try a ittle higher!")
    else:
        print("You guessed it! Well done! :)")
        break
    i += 1
