# [백준 23968번] - 버블 정렬1 - (브론즈1, 버블정렬 알고리즘)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0

def bubble_sort(a):
    
    for i in range(n - 1, 0, -1)
        last = n - 1
        for j in range(n - 1, k, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last
        count += 1

print(count)