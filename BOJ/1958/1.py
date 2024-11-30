a = input().strip()
b = input().strip()
c = input().strip()

dp = [[[0] * (len(a)+1) for _ in range(len(b)+1)] for _ in range(len(c)+1)]

for i in range(len(c)+1):
  for j in range(len(b)+1):
    for k in range(len(a)+1):
      if i == 0 or j == 0 or k == 0:
        dp[i][j][k] = 0
      elif c[i-1] == b[j-1] == a[k-1]:
        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
      else:
        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
ans = 0    
for d in dp:
  for p in d:
    ans = max(ans, max(p))
print(ans)