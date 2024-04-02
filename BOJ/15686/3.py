from itertools import combinations

n, m = map(int, input().split())

chicks = []
home = []
for i in range(n):
  row = list(input().split())
  for j in range(n):
    if row[j] == '1':
      home.append((i, j))
    elif row[j] == '2':
      chicks.append((i, j))

ans = 2 * n * 1000
for c in combinations(chicks, m):
  local_len = 0
  for h in home:
    min_len = 2 * n * 1000
    for ch in c:
      min_len = min(min_len, abs(h[0] - ch[0]) + abs(h[1] - ch[1]))
    local_len+= min_len
  ans = min(ans, local_len)
  
print(ans)