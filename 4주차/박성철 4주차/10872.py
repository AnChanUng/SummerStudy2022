#10872 팩토리얼


import sys
input = sys.stdin.readline


def factorial(n:int)->int:

    if n>0:
        return n*factorial(n-1)
    else:
        return 1

n= int(input())
print(factorial(n))