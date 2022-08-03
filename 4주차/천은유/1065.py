import sys

input = sys.stdin.readline
n = int(input())

c = 0
for i in range(1, n+1):
    if 1 <= i <= 99: # 한 자릿수와 두 자릿수는 모두 한수
        c+=1
    elif i >= 100:
        if ((i % 100) // 10) - (i // 100) == ((i % 100) % 10) - ((i % 100) // 10): # 세자릿수(abc)부터는 b - a = c - b가 같으면 한수  
            c += 1

print(c)
