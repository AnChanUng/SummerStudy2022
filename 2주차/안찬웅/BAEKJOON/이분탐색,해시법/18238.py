# [백준 10816번] ZOAC 2

text = list(map(ord, input()))

result = 0
tmp = 65

for i in text:
    right = tmp - i
    left = i - tmp
    tmp = i

    if right < 0:
        right += 26
    
    if left < 0:
        left += 26

    result += min(right, left)

print(result)