import sys
n = int(input())
f = [0] * (n+1)

if n > 1:
  f[2] = 1
if n > 2:
  f[3] = 1
  
for i in range(4, n+1):
  f[i] = min(f[i-1], (f[i//2] if i%2==0 else n), (f[i//3] if i%3 == 0 else n)) + 1
  
print(f[-1])