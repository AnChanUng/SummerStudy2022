# [백준 24090번] - 퀵 정렬1 - (실버4, 퀵정렬)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 가장 일반적인 퀵 정렬
def quick_sort(array, start, end):
    if start >= end: return # 원소가 1개인 경우
    pivot = start # 피벗은 첫 요소
    left, right = start + 1, end
    
    while left <= right:
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈린 경우
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)