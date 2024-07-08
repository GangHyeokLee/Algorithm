import math

n = int(input())

prime = [2, 3]

for i in range(4, n+1):
  chk = True
  for p in prime:
    if p > math.sqrt(i): break
    
    if i%p == 0:
      chk = False
      break
  if chk:
    prime.append(i)

start = 0
end = 1
tmp = prime[start]
answer = 0

while start < end and end <= len(prime):
  if tmp < n:
    if end < len(prime):
      tmp += prime[end]
    end += 1
  elif tmp >= n:
    if tmp == n:
      answer += 1
    tmp -= prime[start]
    start += 1
    
print(answer)