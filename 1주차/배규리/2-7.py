#10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기(실습 2-7[A] 수정)

def card_conv(x:int, r:int)->str:
    d=''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n=len(str(x))
    print(f'{r:2}|{x:{n}d}')

    while x>0:
        print(' +'+(n+2)*'-')
        if x//r:
            print(f'{r:2}| {x//r:{n}d} --- {x%r}')
        else:
            print(f'    {x//r:{n}d} --- {x%r}')
        d+=dchar[x%r]
        x//=r
    return d[::-1]
while True:
    print('10진수를 n진수로 변환합니다.')
    number = int(input("변환할 값으로 음이 아닌 정수를 입력하세요: "))
    r = int(input('어떤 진수로 변환할까요?: '))
    result = card_conv(number, r)
    print(f'{r}진수로는 {result}입니다.')
    ans=input('한 번 더 변환할까요?(Y---예/N---아니요) :')
    if ans=='N' or ans=='n':
        break
