# [백준 9663번] - N-Queen - (골드4, 8퀸 문제)
import sys

input = sys.stdin.readline

N = int(input())

pos = [0] * N
flag = [False] * N

def put() -> None:

    for i in range(N):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:

    for j in range(N):
        if not flag[j]:
            pos[i] = j
            if i == 7:
                put()
            else:
                flag[j] = True
                set(i + 1) 
                flag[j] = False


set(0)