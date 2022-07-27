import sys

def hanoi(num, start, via, goal):
    if num == 1: # 가장 아래 판인 경우
        print(start, goal) # 시작 기둥에서 목표 기둥으로 옮기기만 하면 됨
    else: # 가장 아래 판을 제외한 나머지 판들
        hanoi(num-1, start, goal, via) # 시작 지점에서 목표 지점을 거쳐 중간 지점으로 이동 
        print(start, goal) # 시작 지점과 목표 지점을 출력
        hanoi(num-1, via, start, goal) # 중간 지점에서 시작 지점을 거쳐 목표 지점으로 이동 

input = sys.stdin.readline
num = int(input())
print(2**num-1)
hanoi(num, 1, 2 ,3)
