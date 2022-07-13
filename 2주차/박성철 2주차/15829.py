

n= int(input())
a=[]
a= input()
sum=0
for k in range(len(a)):
    sum += int(ord(a[k])-96)*(31**k)
print(sum%1234567891)