import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n): # n회 입력 받기
    num, s = map(str, input().split()) # 문자열 반복 횟수와 문자열 입력 받기 
        
    for i in s: # 문자열 내 문자 하나하나를 주목
        print(i*int(num), end='') # num 회 반복한 문자를 출력
    print() # 문자열 바꾸기가 끝나면 다음줄로 커서 이동
