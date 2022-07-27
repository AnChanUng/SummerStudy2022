# [백준 18258번] - 큐2 - (실버4, 큐)
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = deque([])

def push(x):
    que.append(x)

def pop():
    if not que:
        return -1
    else:
        return que.popleft() # 가장앞에 있는 정수빼기

def size():
    return len(que)

def empty():
    return 0 if que else 1

def front():
    if not que:
        return -1
    else:
        return que[0]
def back():
    if not que:
        return -1
    else:
        return que[-1]

for i in range(N):
  input_split = input().split() # 명령어 받는데 split해서 입력받기

  command = input_split[0]      # 명령어 받기

  if command == 'push':
    push(input_split[1])
  elif command == "pop":
    print(pop())
  elif command == "size":
    print(size())
  elif command == "empty":
    print(empty())
  elif command == "front":
    print(front())
  elif command == "back":
    print(back())