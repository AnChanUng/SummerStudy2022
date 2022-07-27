# [백준 12605번] - 단어순서 뒤집기 - (브론즈1, 스택)
import sys
input = sys.stdin.readline

N = int(input())                     # 전체 케이스 개수

for i in range(N):
    L = list(input().split())
    print("Case #%d: "%(i+1), end='', *L[::-1])