def main():
    x = int(input("x: "))
    y = int(input("y: "))
    z = maximum(x, y)
    print("Maximum is", z)

def maximum(a, b):
    if a > b:
        return a #exit a function, or output/return some value of that function
    else:
        return b

main()