# [백준 1110번] - 더하기 사이클 - (브론즈1, 반복문)
import sys
input = sys.stdin.readline

N = int(input())
num = N
count = 0

while True:
  a = num // 10      
  b = num % 10       
  c = (a+b) % 10     
  num = (b*10) + c
  count += 1
  if num == N:
      break

print(count)