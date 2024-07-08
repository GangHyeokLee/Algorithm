n = int(input())

isPrime = [True] * (n+1)
isPrime[0] = isPrime[1] = False
p = 2

while p* p <= n:
  if isPrime[p]:
    for i in range(p*p, n+1, p):
      isPrime[i] = False
  p += 1
  

prime = []
for i, v in enumerate(isPrime):
  if v:
    prime.append(i)

start = 0
end = 0
tmp = 0
answer = 0

while start < len(prime):
  if tmp < n and end < len(prime):
    tmp += prime[end]
    end += 1
  else:
    if tmp == n:
      answer += 1
    tmp -= prime[start]
    start += 1
    
print(answer)