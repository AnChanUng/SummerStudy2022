import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    num, s = map(str, input().split())
        
    for i in s:
        print(i*int(num), end='')
    print()
