def main():
    score1 = int(input("Score 1: "))
    score2 = int(input("Score 2: "))
    score3 = int(input("Score 3: "))

    print_scores(score1)
    print_scores(score2)
    print_scores(score3)

def print_scores(n):
    for i in range(n):
        print("#",end="") #after the hash mark(#) don't print anything, just print nothing.
    print( ) #prints new line

main()