k=int(input())    #k변수로 정수 입력받기
l=[]              #l변수로 빈 리스트 생성

for i in range(k):   #for문으로 k줄의정수를 입력받기
    b=int(input())
    if b == 0:       #받은수가 0일때 이를 pop함으로써 지움
        l.pop()
    else:
        l.append(b)   #그외에는 추가함으로 append

result=sum(l)      #resulut배열이만들어지고 이를 출력함
print(result)