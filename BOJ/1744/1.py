n = int(input())


pos = []
zero = 1
neg = []

for _ in range(n):
  t = int(input())
  
  if t > 0:
    pos.append(t)
  elif t < 0:
    neg.append(t)
  else:
    zero = 0
    

neg.sort(reverse=True)
pos.sort()

ans = 0

while len(pos) > 1:
  a = pos.pop()
  b = pos.pop()
  
  if a == 1 or b == 1:
    ans += a + b
  else:
    ans += a * b

if pos:
  ans += pos.pop()

while len(neg) > 1:
  ans += neg.pop() * neg.pop()

if neg:
  ans += neg.pop() * zero

print(ans)