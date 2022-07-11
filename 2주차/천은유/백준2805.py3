import sys

input = sys.stdin.readline
n, m = map(int, input().split()) # n: 나무개수, m: 필요한 미터 
data = list(map(int, input().split())) # 나무들의 미터

pl, pr = 1, max(data) # 왼쪽 범위와 오른쪽 범위 설정

while pl<=pr: # 왼쪽 범위가 오른쪽 범위보다 크면 종료
    hap = 0 # 높이
    pc = (pl+pr)//2 # 중앙값 설정

    for a in data: # 높이 찾기
        # 탐색값이 중앙값 보다 크면, 높이 = 탐색값-중앙값
        hap += a - pc if a > pc else 0 
    
    if hap >= m: # 높이가 m미터보다 크거나 같으면
        pl = pc + 1 # 왼쪽 값 = 중앙값 + 1
    else: # 높이가 m 미터보다 작으면
        pr = pc - 1 # 오른쪽 값 = 중앙값 - 1

print(pr)