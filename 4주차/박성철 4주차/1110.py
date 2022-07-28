#1110  더하기 사이클

import sys
input=sys.stdin.readline

n = int(input())
nList = list(map(int, str(n))) # 배열로 변환
cnt = 0

def cycle(nList, n):
    result = list(map(int, str(sum(nList))))
    hap = nList[-1] * 10 + result[-1] # 기존숫자의 오른쪽과, 합한 숫자의 오른쪽 더하기
    global cnt
    cnt += 1
    if hap == n:
        print(cnt)
    else:
        hap = list(map(int, str(hap)))
        cycle(hap, n)


cycle(nList, n)