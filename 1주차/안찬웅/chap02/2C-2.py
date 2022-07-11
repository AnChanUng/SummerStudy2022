# [실습2C-2] #리스트의 모든 원소를 enumerate()함수로 스캔하기
"""emurate함수는 인덱스와 원소를 짝지어 튜플로 꺼내는 내장함수"""

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')