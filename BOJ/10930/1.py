import hashlib

S = input().encode()
s = hashlib.sha256(S).hexdigest()

print(s)
