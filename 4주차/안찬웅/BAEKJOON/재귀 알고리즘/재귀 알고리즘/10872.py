# [백준 10872번] - 팩토리얼 - (실버4, 스택)

def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼값을 재귀적으로 구함"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input())
    print(factorial(n))