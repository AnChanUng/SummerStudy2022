import sys

input = sys.stdin.readline
T = int(input()) # 입력 개수 받기

for i in range(T): # T번 반복하며 판정하기
    stack = [] # 빈 배열 생성
    parenthesis_string = input().rstrip()

    for j in parenthesis_string:
        if j == '(':                # '('문자일 경우 스택에 append
            stack.append(j)
        elif j == ')':              # ')'문자일 경우
            if stack:               # 스택에 자료('(')가 있으면 가장 마지막 '('를 pop
                stack.pop()
            else:                   # 스택에 자료가 없을경우는 "NO" 출력후 탈출
                print("NO")
                break
    else:                           # break문으로 탈출하지 않을 경우
        if not stack:               # 스택이 비어있는 경우 "YES" 출력
	        print("YES")
        else:                       # 스택이 남아있는 경우 "NO"출력
	        print("NO")
