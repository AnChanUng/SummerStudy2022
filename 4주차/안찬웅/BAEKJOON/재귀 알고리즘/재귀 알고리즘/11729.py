# [백준 11729번] - 하노이 탑 이동 순서 - (실버1, 하노이 탑)
import sys
input = sys.stdin.readline

def move(no, x, y):
    """원반 no개를 x기둥에서 y기둥으로 옮김"""
    if no > 1:
        move(no - 1, x, 6 - x - y)      # 기둥이 1개 이상이면 그룹으로 묶인 n-1개 원판을 
                                        # 중간으로 먼저 모두 옮김

    print(x, y)

    if no > 1:
        move(no - 1, 6 - x - y, y)

n = int(input())

print(2**n -1)                          # 이동한 총 횟수
move(n, 1, 3)                           # 1기둥에 쌓인 원반 no개를 3기둥으로 옮김