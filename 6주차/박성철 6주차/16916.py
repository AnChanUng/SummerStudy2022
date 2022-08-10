#16916 부분 문자열

# 교재 313p 참고
txt = input()
pat = input()

pt = 1
pp = 0
skip = [0]*(len(pat)+1)

skip[pt] = 0
while pt != len(pat):
    if pat[pt] ==pat[pp]:
        pt +=1
        pp+=1
        skip[pt] =pp
    elif pp==0:
        pt+=1
        skip[pt] =pp
    else:
        pp = skip[pp]


pt = pp = 0
while pt!=len(txt) and pp!= len(pat):
    if txt[pt] ==pat[pp]:
        pt+=1
        pp+=1
    elif pp ==0:
        pt+=1
    else:
        pp=skip[pp]

if pp==len(pat):
    print(1)
else:
    print(0)