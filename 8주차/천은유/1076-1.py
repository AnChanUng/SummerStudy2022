color = ['black', 'brown', 'red', 
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

f = color.index(input()) # 인덱스 반환
s = color.index(input()) # 인덱스 반환
t = color.index(input()) # 인덱스 반환

r = int(str(f) + str(s)) * (10 ** t) # f+s를 저장 후 10의 t제곱과 곱함
print(r)
