# [백준 2675번] - 문자열 반복 - (브론즈2, 문자열)
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)
    for i in range(len(S)):
        print(R * S[i], end='')
    print()