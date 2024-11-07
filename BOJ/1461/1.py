n, m = map(int, input().split())

pb = []
nb = []

for b in map(int, input().split()):
  if b < 0:
    nb.append(-b)
  else:
    pb.append(b)
    
nb.sort()
pb.sort()
dp = [-1] * len(nb)

i = 0
while i < m and i < len(nb):
  dp[i] = nb[i]
  i+=1

# 점화식: dp[n] = min(dp[n-m] + books[n-m] + books[n], dp[n-1] + books[n-1] + books[n]) ## n-m까지 책 갖다넣고 0으로 간 다음에 n-m+1... n-1, n가기 vs n-1까지 책 넣고 0으로 가서 n가기
ans = 0
for i in range(m, len(dp)):
  dp[i] = dp[i-m] + nb[i-m] + nb[i]
  
  b = m-1
  while b >= 1:
    dp[i] = min(dp[i], dp[i-b] + nb[i-b] + nb[i])
    b-=1
if dp:
  ans += dp[-1]


dp = [-1] * len(pb)
i = 0
while i < m and i < len(pb):
  dp[i] = pb[i]
  i+=1

for i in range(m, len(dp)):
  dp[i] = dp[i-m] + pb[i-m] + pb[i]
  b = m-1
  while b >= 1:
    dp[i] = min(dp[i], dp[i-b] + pb[i-b] + pb[i])
    b-=1
if dp:
  ans += dp[-1]

print(ans + min(pb[-1] if pb else 0, nb[-1] if nb else 0))