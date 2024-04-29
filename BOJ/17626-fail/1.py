import math

n = int(input())

# pd와 그리디
dp = [0] * (n+1)
dp[1] = 1

for i in range(1, n+1):
  tmp = i
  j=1
  while (j**2) <= i:
    tmp = min(tmp, dp[i-(j**2)])
    j+=1
  dp[i] = tmp+1
    

print(dp[-1])