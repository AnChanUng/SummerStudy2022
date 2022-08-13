# [백준 2798번] - 블랙잭 - (브론즈2, 문자열검색)
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
sum = 0

for i in range(N):
  for j in range(i+1, N):
      for k in range(j+1, N):
          if a[i] + a[j] + a[k] > M:
              continue
          else:
              sum = max(sum, a[i]+a[j]+a[k])
print(sum)