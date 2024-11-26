n, m = map(int, input().split())

bus = [list(map(int, input().split())) for _ in range(m)]
max_cost = 500 * 6000 * 30000

dp = [max_cost] * (n+1)
dp[1] = 0

chk = False

# n번 반복
# 음의 값을 가진 사이클이 없다면 n-1번만 업데이트하고 끝날 것
# 음의 값을 가진 사이클이 있다며 n-1번 이후에도 업데이트가 일어날 것
for i in range(1, n+1):
  for a, b, c in bus:
    if dp[a] == max_cost:
      continue
    
    if dp[a] + c >= dp[b]: continue
    dp[b] = dp[a] + c
    if  i == n:
      chk = True
      
if chk:
  print(-1)
else:
  for i in range(2, n+1):
    print(dp[i] if dp[i] < max_cost else -1 )
  