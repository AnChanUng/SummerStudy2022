#9663 N-Queen


import sys
input = sys.stdin.readline

n = int(input())

cn=0

flag_a =[False]*n
flag_b =[False]*(n*2-1)
flag_c =[False]*(n*2-1)

def set(i:int)->None:
    """열과 퀸 갯수를 받음"""

    for j in range(n):
        if(not flag_a[j] and not flag_b[i+j]
        and not flag_c[i-j+n-1]):

            if i== n-1:
                global cn
                cn+=1 # 하나의 배치도가 완성되면 cn을 1씩 증가
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1]=True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+n-1]=False

set(0)
print(cn)
