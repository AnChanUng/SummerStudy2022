from multiprocessing.sharedctypes import Value
from typing import Any

class FixedStack:

    def empty(self) ->bool:
        return self.ptr <=0


    def size(self) ->int:
        return self.ptr

    def push(self, value:Any) ->None:
        self.stk[self.ptr]=Value
        self.ptr+=1
    def pop(self)->Any:
        self.ptr-=1
        return self.stk[self.ptr]
        if self.empty():
            return -1

     
    def top(self):
        if len(self)>0:
            print(self[-1])
        else :
            print(-1)        

n=int(input()) #명령 수
N= [input() for _ in range(n)] #명령입력

for i in range(n):
    if "push" in N[i]:
        push(N[i].split()[1])
    elif N[i] == "top":
        top(self)
    elif N[i] == "size":
        size(self)   
    elif N[i] == "empty":
        empty(self)   
    elif N[i] == "pop":
        pop(self)   
