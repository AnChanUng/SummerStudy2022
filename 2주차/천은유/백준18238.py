zoac = input()
lastchar = 'A' # 마지막 문자
result = 0

for i in list(zoac): #문자를 아스키코드화
  a = abs(ord(i) - ord(lastchar)) # 현재 문자 - 마지막 문자를 절댓값으로 저장
  lastchar = i # 마지막 문자는 i
  result += min(a, 26 - a) # 시계 방향과 반시계 방향으로 돌리는 것 중 작은 값을 선택하여 저장

print(result)
