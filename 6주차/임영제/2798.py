n, m = map(int, input().split()) #n,m을 입력받아 int로변환한다.
a = list(map(int, input().split())) #카드에 쓰여있는 수들을list화하여 저장
b = len(a)
sum = 0
for i in range(0, b - 2):  #3개의 카드를뽑아야 하며이에 대한모든경우의수를 살펴보기위해3중for문이용
        for j in range(i + 1, b - 1):
                for k in range(j + 1, b):
                        if a[i] + a[j] + a[k] > m:
                                continue
                        else:
                                sum = max(sum, a[i] + a[j] + a[k])
print(sum)#sum값출력
