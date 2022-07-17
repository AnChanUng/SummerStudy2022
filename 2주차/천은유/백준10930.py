import sys, hashlib

str1 = sys.stdin.readline().rstrip()
# str1 바이트 문자열을 생성하여 해시값을 구한 후 16진수로 변환하여 출력
res = hashlib.sha256(str1.encode()).hexdigest()
print(res)
