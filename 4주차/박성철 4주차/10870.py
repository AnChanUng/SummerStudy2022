#10870 피보나치 수 5

import sys
input = sys.stdin.readline

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))