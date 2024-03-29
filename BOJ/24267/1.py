n = int(input())
ans = 0
for i in range(3, n+1):
  ans += (i-1) * (i-2) // 2
  
print(ans)
print(3)