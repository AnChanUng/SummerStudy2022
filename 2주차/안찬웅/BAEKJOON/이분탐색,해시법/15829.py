# [백준 15829번] Hashing

L = int(input())  
string = input()   
result = 0
M = 1234567891

for i in range(L):
    result += (ord(string[i])-96) * (31 ** i)
    print(result % M)