n = int(input())

ans = 0
while n > 0:
  k = 1
  while k * (k+1)  <= 2 * n:
    k+=1
  if k > 1:
    n = n - int(k *(k-1) / 2)
    ans += k-1
  else:
    n = n-1
    ans += 1

print(ans)
