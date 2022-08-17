import sys

input = sys.stdin.readline
s = input().rstrip()

for i in range(0, len(s)):
    print(s[i], end='')
    if i % 10 == 9:
        print()
