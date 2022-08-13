#2798 블랙잭

import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sum = num[i]+num[j]+num[k]
            if sum<=m:
                result = max(result,sum)

print(result)