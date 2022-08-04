# [백준 23881번] - 선택 정렬1 - (브론즈1, 선택정렬 알고리즘)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())     # A:배열의 크기 k:교환횟수
a = list(map(int, input().split()))
count = 0

def selection_sort(a):
    """단순 선택 정렬"""
    for i in range(n - 1, 0, -1):
        max = i
        for j in range(i + 1):
            if a[j] > a[max]:
                max = j

        if max != i:
            a[i], a[max] = a[max], a[i]
            count += 1
        
        if count == k:
            return str(a[max]) + " " + str(a[i])
        
    return -1

print(selection_sort)