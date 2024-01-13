n = int(input())

ans = 0
for i in range(n // 2+1):
  ones = i*2 + n%2
  twos = n // 2 - i
  tp = 1
  for j in range(1, ones+twos+1):
    tp *= j
  for j in range(1, ones+1):
    tp //= j
  for j in range(1, twos+1):
    tp //= j
  ans += tp
    
print(ans%10007)