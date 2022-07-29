#1065 한수

import sys
input=sys.stdin.readline

n = int(input())
count = 0
for i in range(1, n + 1):
    if i < 100:  # 100보다 작으면 항상 등차수열
        count += 1
    else:
        ns = list(map(int, str(i))) # 각 자리의 수를 배열로 구분
        if ns[0] - ns[1] == ns[1] - ns[2]: # 등차인지 확인
            count += 1
print(count)