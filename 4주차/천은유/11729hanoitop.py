import sys

def hanoi(num, start, via, goal):
    if num == 1:
        print(start, goal)
    else:
        hanoi(num-1, start, via, goal)
        print(start, goal)
        hanoi(num-1, via, start, goal)

input = sys.stdin.readine
n = int(input())
print(2**num-1)
hanoi(num, 1, 2 ,3)
