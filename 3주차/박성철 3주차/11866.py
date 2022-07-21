# 11866 요세푸스 문제0

import sys
input = sys.stdin.readline
n,k = map(int, input().split())
list = [i for i in range(1,n+1)]
i=0

print("<",end="")
while len(list)>1:
    i=i+k

    if i>len(list):
        i=i%len(list)
        if i==0:
            i = i+len(list)
    i =i-1
    print(str(list.pop(i)),end=", ")
print(str(list.pop())+">")
