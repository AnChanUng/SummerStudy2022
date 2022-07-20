from hashlib import sha256

data = input()

print(sha256(data.encode()).hexdigest())
