n = int(input())#입력받기

ans = 0#출력의 초기값
row = [0] * n #1차원배열의인덱스와 값을통해위치기록

def is_promising(x):#같은열에다른퀸이 있는경우,대각선에 다른퀸이 있는경우 false출력 그외에는 true출력하는 is_promising함수생성
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x): #n_queens함수생성
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):#퀸 놓는위치가 is_promising하면
                n_queens(x+1)#다음퀸을 놓기위한 n_queens(i+1)을호출

n_queens(0)
print(ans)