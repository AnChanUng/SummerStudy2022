# [백준 10930번] SHA-256
import hashlib

string = input()
encoded = string.encode()
result = hashlib.sha256(encoded).hexdigest()
print(result)