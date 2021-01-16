# Asks for an integer (n) & shows a n by n grid made up of #'s'

def main():
    n = int(input("Number: "))
    grid(n)


def grid(n):
    for i in range(n):
        for j in range(n):
            print("#", end="")
        print()



main()