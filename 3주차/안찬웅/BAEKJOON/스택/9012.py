# [백준 9012번] - 괄호 - (실버4, 스택)
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    stack = []
    for i in input().rstrip():
        if i == "(":
            stack.append(i)
        else:
            try:
                stack.pop()
            except:
                print("NO")
                break
                
    else:             
        print("NO" if stack else "YES")