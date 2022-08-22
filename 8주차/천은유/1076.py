import sys

input = sys.stdin.readline
colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'] 

s = 0
s += colors.index(input().rstrip())*10 
s += colors.index(input().rstrip())
for _ in range(colors.index(input().rstrip())):
    s *= 10

print(s)
