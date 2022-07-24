import sys

input = sys.stdin.readline
n, k = map(int, input().split())
que = [i for i in range(1, n+1)]
res = []
pt = 0

for _ in range(n):
    pt += k - 1 # 배열은 0부터 시작하기 때문에 k - 1
    pt %= len(que) # que 배열의 크기를 pt 변수로 나눈 후의 나머지
    res.append(que.pop(pt)) # que 배열 pt 인덱스를 pop하여 res 배열에 추가
    
print(f"<{', '.join(map(str, res))}>") # res 배열을 f-string을 이용하여 한꺼번에 출력
