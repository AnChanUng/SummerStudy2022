#11721 열 개씩 끊어 출력하기

m = input()
for i in range(0,len(m)):
    print(m[i],end='')
    if (i+1)%10 ==0:
        print()

