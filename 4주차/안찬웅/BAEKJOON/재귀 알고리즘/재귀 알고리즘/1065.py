# [백준 1065번] - 한수 - (실버4, 브루트포스 알고리즘)
import sys
input = sys.stdin.readline

n = int(input())
hansu = 0

for n in range(1, n+1): # 1부터 99까지는 모두 한수
    if n <= 99:
        hansu += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] - nums[1] == nums[1] - nums[2]: # 숫자를 자릿수대로 분리
            hansu += 1                             # 등차수열 확인
print(hansu)