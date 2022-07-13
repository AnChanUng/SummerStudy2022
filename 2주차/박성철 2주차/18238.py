a= input() # 문자열 입력

result=0
if abs(int(ord('A')-ord(a[0])))<13:  # 'A'와 첫번째 문자의 최소거리를 result에 더함
    result+=abs(int(ord('A')-ord(a[0])))
else :
    result+= 26-abs(int(ord('A')-ord(a[0])))

for i in range(len(a)-1): # 입력받은 문자끼리의 최소거리를 result에 더함
    k=abs(int(ord(a[i])-ord(a[i+1])))
    if k<13:
        result+=k
    else :
        result+= 26-k
print(result)