# [백준 10816번] - 숫자카드2 - 이분탐색
import sys
input = sys.stdin.readline

N = int(input())
a = [*map(int, input().split())]
M = int(input())
b = [*map(int, input().split())]

count = {}
for i in a:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in b:
    if i in count:
        print(count[i], end= " ")
    else:
        print(0, end=" ")

# key: 카드의 숫자
# value: 카드의 개수
