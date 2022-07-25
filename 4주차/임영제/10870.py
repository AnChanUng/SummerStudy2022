
import sys 
sys.setrecursionlimit(100000)
n=int(sys.stdin.readline())

def fibonacci(n):
   if n <=1:
    return n
   else :
    return fibonacci(n-2)+fibonacci(n-1)

print (fibonacci(n))
