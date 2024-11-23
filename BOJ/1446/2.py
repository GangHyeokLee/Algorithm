from collections import defaultdict

n, d = map(int, input().split())

short = defaultdict(list)

for _ in range(n):
  start, end, length = map(int, input().split())
  
  short[end].append((start, length))
  

dp = [10000 * n * d] * (d+1)
dp[0] = 0

# 점화식
# dp[n] = min(dp[n-1] + 1, short[n][1] + dp[short[n][0]])
for i in range(1, d+1):
  dp[i] = dp[i-1] + 1
  
  for start, cost in short[i]:
    dp[i] = min(dp[i], cost + dp[start])
      
  
print(dp[-1])