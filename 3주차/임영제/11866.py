from collections import deque#deque사용하기 위한 코드
n, k = map(int, input().split())#n,k map을 이용하여 정수형 입력을 나눠받는다
s = deque([])#s는 덱으로 설정
for i in range(1, n + 1): #1~n까지의 수를 s라는 deque에 담기
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):   #s안의 값이 있는 동안 k-1번 동안 s의 첫번째 원소를 제거하여 출력해야하는 k번째 요소 출력
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:         #만약 s에 요소가있다면 컴마 붙여서 print하고 없다면 (마지막것이 방금 출력되어) 그냥 출력되고 >가 붙어 마무리된다.
        print(', ', end='')
print('>')