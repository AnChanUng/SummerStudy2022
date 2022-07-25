import sys

def Fibonacci(n): # 피보나치 수열 함수
    if n == 0: # n이 0이면 0 반환
        return 0
    elif n == 1: # n이 1이면 1 반환
        return 1
    else: # n이 2 이상이면
        return Fibonacci(n-1) + Fibonacci(n-2) 

input = sys.stdin.readline
n = int(input())
print(Fibonacci(n))
