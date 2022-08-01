# [백준 10866번] - 덱 - (실버4, 덱)
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = deque([])

def push_front(x):
    que.appendleft(x)

def push_back(x):
    que.append(x)

def pop_front():
    if not que:
        return -1
    else: 
        return que.popleft()

def pop_back():
    if not que:
        return -1 
    else:
        return que.pop()

def size():
    return len(que)

def empty():
    if not que:
        return 1
    else:
        return 0

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
  input_split = input().split()

  command = input_split[0]

  if command == 'push_front':                                                                                                                          
    push_front(input_split[1])
  elif command == "push_back":
    push_back(input_split[1])
  elif command == "pop_front":
    print(pop_front())
  elif command == "pop_back":
    print(pop_back())
  elif command == "size":
    print(size())
  elif command == "empty":
    print(empty())
  elif command == "front":
    print(front())
  elif command == "back":
    print(back())