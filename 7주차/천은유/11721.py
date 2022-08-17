import sys

input = sys.stdin.readline
s = input().rstrip()

for i in range(0, len(s)):
    if i % 10 == 9:
        print(s[i], end='\n')
    else:
        print(s[i], end='')
