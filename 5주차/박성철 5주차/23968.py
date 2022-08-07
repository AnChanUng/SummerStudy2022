#23881 알고리즘 수업- 선택 정렬1

import sys
n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0
answer = -1

for i in range(n-1, 0, -1):
    for j in range(i):
        if num[j] > num[j+1]:
            cnt += 1
            num[j], num[j+1] = num[j+1], num[j]

            if cnt == k:
                answer = f'{num[j]} {num[j+1]}'

print(answer)