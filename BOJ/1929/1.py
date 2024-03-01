import math

m, n = map(int, input().split())

primes = [2, 3, 5, 7, 11]

for i in range(12, n+1):
  chk = True
  for p in primes:
    if p > math.sqrt(i): break
    if i % p == 0:
      chk = False
      break
  if chk:
    primes.append(i)

for i in primes:
  if i > n:
    break
  
  if i >= m:
    print(i)