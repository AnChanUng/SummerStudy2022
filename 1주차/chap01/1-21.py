# [실습1-21] 구구단 곱셈표 출력하기

print('-' * 27)
for i in range(1, 18):                # 행
    for j in range(1, 10):            # 열
        print(f'{i * j:3}', end='')   
    print()                           # 행 변경
print('-' * 27)