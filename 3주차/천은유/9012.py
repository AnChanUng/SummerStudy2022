import sys

T = int(sys.stdin.readline())

for i in range(T):
    stack = []
    parenthesis_string = sys.stdin.readline().rstrip()

    for j in parenthesis_string:
        if j == '(':                # '('문자일 경우 스택에 append
            stack.append(j)
        elif j == ')':              # ')'문자일 경우
            if stack:               # 스택에 자료가 있으면 pop
                stack.pop()
            else:                   # 스택에 자료가 없을경우 "NO" 출력후 탈출
                print("NO")
                break
    else:                           # break문으로 탈출하지 않을 경우
        if not stack:               # 스택이 비어있는 경우 "YES" 출력
	        print("YES")
        else:                       # 스택이 남아있는 경우 "NO"출력
	        print("NO")
