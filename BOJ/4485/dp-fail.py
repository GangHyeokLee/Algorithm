def dpf(i, j, dp, cave, n):
  if dp[i][j] == n * n * 100:
    up = dpf(i-1, j, dp, cave, n) if i > 0 else n * n * 1000
    left = dpf(i, j-1, dp, cave, n) if j > 0 else n * n * 1000
    down = dpf(i+1, j, dp, cave, n) if i + 1 < n else n * n * 1000
    right = dpf(i, j+1, dp, cave, n) if j + 1 < n else n * n * 1000
    
    dp[i][j] = cave[i][j] + min(left, up, right, down)
    
  return dp[i][j]

count = 1
while True:
  n = int(input())
  
  if n == 0:
    break
  cave = list(list(map(int, input().split())) for _ in range(n))
  
  dp = [[n * n * 100] * n for _ in range(n)]
  dp[0][0] = cave[0][0]
  
  # 점화식
  # dp[n][n] = min(dp[n-1][n], dp[n][n-1]) + cave[n][n]

  
  print('Problem '+str(count)+ ":",  dpf(n-1, n-1, dp, cave, n))
  
  for d in dp:
    print(d)
  count += 1