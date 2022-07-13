from hashlib import sha256

a = input()

print(sha256(a.encode()).hexdigest())