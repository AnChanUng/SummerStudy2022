# [백준 10828번] - 스택 - (실버4, 스택)
import sys
input = sys.stdin.readline
def push(x):
    stack.append(x)

def pop():
    if(not stack):
        return -1
    else:
        return stack.pop()
def size():
  return len(stack)
  
def empty():
  return 0 if stack else 1

def top():
  return stack[-1] if stack else -1

N = int(input())
stack = []

for i in range(N):
  input_split = input().split() # 명령어 받는데 split해서 입력받기

  command = input_split[0] # 명령어 받기

  if command == 'push':
    push(input_split[1])
  elif command == "pop":
    print(pop())
  elif command == "size":
    print(size())
  elif command == "empty":
    print(empty())
  elif command == "top":
    print(top())