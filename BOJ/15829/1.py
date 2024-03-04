
r = 31
M = 1234567891

n = int(input())
texts = input()

ans = 0

for i in range(n):
  ans += (ord(texts[i])-96) * (r ** i)
  
print(ans % M)