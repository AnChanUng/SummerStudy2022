#23881 알고리즘 수업- 선택 정렬1

import sys
input=sys.stdin.readline

from typing import MutableSequence

def selection_sort(a: MutableSequence, b:int) -> None:
    cnt=0 # 카운트 할 변수
    n = len(a)
    for i in range(n-1,0,-1): # 마지막 인덱스부터 역순으로
        max=i
        for j in range(i):
            if a[j]>a[max]: # 마지막 값보다 크면 해당 인덱스를 max로
                max = j
        if a[max]!=a[i]: # 교환할 값이 있으면 수행
            cnt +=1 # 카운트 +1
            a[i],a[max] = a[max],a[i] # 교환
            if cnt==b: # 카운트의 값과 초기에 입력받은 b값과 같으면 교환한 두개의 정수를 출력
                print(f'{a[max]} {a[i]}')

    if cnt<b: # b값이 교환횟수보다 크면 -1 출력
        print(-1)


n = input().split()
arr = list(map(int,input().split()))

selection_sort(arr,int(n[1]))




