import sys

def factorial(n): # 팩토리얼 재귀 함수
    if n > 0: # n이 자연수면
        return n * factorial(n-1) # n x (n-1)! 수행
    else: # n이 0이하면
        return 1 # 1 출력

input = sys.stdin.readline
n = int(input())
print(factorial(n))
