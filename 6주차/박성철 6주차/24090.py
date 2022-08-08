# 24090 알고리즘 수업 - 퀵 정렬1

from typing import MutableSequence

def qsort(a:MutableSequence, left: int, right:int,k:int) ->None:
    global cnt
    pl = left
    pr = right
    x= a[(left+right)//2]

    while pl<=pr:
        while a[pl]<x:pl+=1
        while a[pr] > x:pr -=1
        if pl<=pr:
            a[pl],a[pr]=a[pr],a[pl]
            cnt+=1
            if cnt==k:
                print(f'{a[pl]} {a[pr]}')
            pl+=1
            pr-=1
    if left<pr:qsort(a,left,pr,k)
    if pl <right:qsort(a,pl,right,k)


def quick_sort(a:MutableSequence,k:int)->None:
    qsort(a,0,len(a)-1,k)

import sys
n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

cnt=0

quick_sort(num,k)
if cnt<k:
    print(-1)