# [백준 10870번] - 팩토리얼 - (브론즈5, 피보나치 수열)
import sys
input = sys.stdin.readline

n = int(input())

def fibo(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2) 

print(fibo(n))