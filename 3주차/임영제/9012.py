t=int(input())   #t변수로 테스트하는 케이스하는 수만큼 입력을 받는다

for _ in range(t):    #t경우만큼
    check=input()    #check할 문자열 입력받기
    l=list(check)    #check로 받은 문자열 l변수로list로 입력을 받는다
    sum=0
    for i in l:
        if i == "(":
            sum+=1
        elif i ==")":
            sum-=1
        if sum<0:
            print("NO")
            break
    if sum>0:
        print("NO")
    elif sum ==0:
        print("YES")            
        #if문을 살펴보면 "(" ")"이 같은 숫자만큼 나타나야 sum 이 0이 되서 yes로 성립한다. 이를 for문을 이용한 알고리즘으로 구현한것이다.
            