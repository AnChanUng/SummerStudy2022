import sys
stk = []

def push(item):
    stk.append(item)

def pop():
    if len(stk) == 0:
        print(-1)
    else:
        print(stk[-1])
        stk.pop()

def size(stk):
    print(len(stk))

def empty(stk):
    if len(stk) == 0 :
        print(1)
    else :
        print(0)
        
def top(stk):
    if len(stk) > 0 :
        print(stk[-1])
    else:
        print(-1)

input = sys.stdin.readline
n = int(input())
N = [input().rstrip() for _ in range(n)]

for i in range(n):
    if "push" in N[i]:
        push(N[i].split()[1])
        
    elif N[i] == "top":
        top(stk)
        
    elif N[i] == "size":
        size(stk)
        
    elif N[i] == "empty":
        empty(stk)
        
    elif N[i] == "pop":
        pop()
