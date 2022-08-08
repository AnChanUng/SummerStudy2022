# [백준 24051번] - 삽입 정렬1 - (브론즈1, 삽입정렬 알고리즘)
from os import TMP_MAX
from re import I
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0

def insertion_sort(a):

    for i in range(1, n:
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
        count += 1

print(count)
