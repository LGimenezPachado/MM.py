import numpy as np
import matplotlib as mp

def point(a, b, c):
    print(f"the point will be shown {c} times")
    print("")
    
    for i in range(c):
        print(f"({a};{b})")
        print("")

def pause():
    input("press enter to begin")

def main():
    pause()
    
    x = float(input("enter the value of x position\n"))
    y = float(input("enter the value of y position\n"))
    n = int(input("enter the number of times the point will be shown\n"))
    
    point(x, y, n)

if __name__ == "__main__":
    main()
