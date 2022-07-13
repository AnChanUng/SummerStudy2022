import sys
input = sys.stdin.readline
L = int(input()) # 문자열 길이
str1 = list(input().rstrip()) # 문자열을 입력받아 리스트로 저장

r = 31 # 곱하는 수
M = 1234567891 #나누는 수
res = 0 # 결과 초기화

for i in range(L): # 알파벳을 아스키코드 변환 후 96 빼기(소문자)
    res += (ord(str1[i])-96)*(r**i)

print(res % M)
