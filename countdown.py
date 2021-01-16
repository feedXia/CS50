import random #import the random module from the python library

# Countdown to the new year
def main(): # "def" defines a function I create
    number = random.randint(5,15)
    countdown(number)
    print("Happy New Year!")

def countdown(n):
    for i in range(n):
        print(n - i)


main()