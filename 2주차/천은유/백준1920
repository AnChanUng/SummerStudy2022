import sys
def binary_search(arr, target, start, end): # 이진 탐색
    while start <= end: # 시작 인덱스가 마지막 인덱스보다 작거나 같을 때까지 반복
        mid = (start+end)//2 # 중앙값 설정
        if arr[mid] == target: # 중앙값과 타겟이 같다면
            return 1 # 1 반환
        elif arr[mid] > target: # 중앙값이 타겟값보다 크다면
            end = mid - 1 # 종료 인덱스를 수정
        else: # 중앙값이 타겟값보다 작다면
            start = mid + 1 # 시작 인덱스를 수정
    return 0 # 배열 안에 수가 없는 경우 0 반환
    
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort() # 배열을 오름차순 정렬
m = int(input())
targets = list(map(int, input().split()))
for target in targets: # 타겟 배열 반복문 설정
    print(binary_search(arr, target, 0, n-1)) # 탐색 시작
    
