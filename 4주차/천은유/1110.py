import sys

input = sys.stdin.readline
n = int(input())
c = 0 # 카운트 변수
nn = n # 입력값 저장

while nn != n or c == 0: # n이 입력값과 같아질 때까지 반복
    if n < 10: # n이 10보다 작은 경우
        n = (n*10) + n # n이 한 자릿수면 nn이 됨 (6이면 66이 됨)
        c+=1 # 카운트 1 증가

    else: # 두 자릿수인 경우
        n = ((n // 10) + (n % 10))%10 + (n % 10)*10 # 26 -> 2 + 6 = 8 -> 6 + 8 = 14 -> 8 + 4 = 12
        c+=1 # 카운트 1 증가

print(c)
