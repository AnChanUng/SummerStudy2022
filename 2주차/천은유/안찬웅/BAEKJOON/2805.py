# [백준 2805번] 나무자르기-이분탐색

N, M = map(int, input().split()) # N:나무의수 M:나무의 길이
tree = list(map(int, input().split())) #tree:나무의 높이
start, end = 1, max(tree) # 이분탐색 검색 범위 설정
                          # start:가장길이가 짧은 길이 end:나무중 가장 긴 길이
while start <= end:       # 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
            
    # 벌목높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)