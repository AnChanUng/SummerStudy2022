import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

hashmap = {} # 딕셔너리 형태
for i in a: 
    if i in hashmap:
        hashmap[i] += 1 # 중복된 수가 있으면 1 추가
    else: # 중복이 없는 경우
        hashmap[i] = 1 

for i in b:
    if i in hashmap: # b 리스트에 있는 값이 hashmap에 있는 경우 카운트 수 출력
        print(hashmap[i], end=" ")
    else: # 없는 경우 0 출력
        print(0, end=" ")
print()
