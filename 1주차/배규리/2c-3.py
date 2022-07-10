#리스트의 모든 원소를 enumerate()함수로 스캔하기(1부터 카운트)
x=['John','Geroge','Paul','Ringo']
for i, name in enumerate(x,1): #enumerate는 인덱스와 원소를 함께 꺼내줄 수 있게해줌
    print(f'{i}번째={name}')
