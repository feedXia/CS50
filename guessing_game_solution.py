import random

def main():
    number = random.randint(1, 10)

    for i in range(3):
        guess = int(input("Guess: "))
        if guess > number:
            print("Guess is too large")
        elif guess < number:
            print("Guess is too small")
        else
            print("Correct!")
            return # gets out of the function

main()