# 11729 하노이 탑

import sys
input = sys.stdin.readline

global cn
cn=0

def count(no:int,x:int,y:int) -> None:
    """옮긴 횟수 cn을 카운트하기 위함"""
    global cn
    mid = 6-x-y
    if no>1:
        count(no-1,x,mid)

    cn+=1

    if no>1:
        count(no-1,mid,y)

def move(no:int,x:int,y:int)->None:
    """옮기는 과정을 출력하기 위함"""
    mid = 6-x-y
    if no>1:
        move(no-1,x,mid)

    print(f"{x} {y}")

    if no>1:
        move(no-1,mid,y)

n = int(input())
count(n,1,3)
print(cn)
move(n,1,3)