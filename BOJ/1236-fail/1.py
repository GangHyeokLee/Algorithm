n, m = map(int, input().split())

castle = []

r = [False] * n
for i in range(n):
  row = input()
  if 'X' in row:
    r[i] = True
  castle.append(row)


c = [False] * m
for j in range(m):
  for i in range(n):
    if castle[i][j] == 'X':
      c[j] = True

rf = []
cf = []

for idx, v in enumerate(r):
  if not v:
    rf.append(idx)

for idx, v in enumerate(c):
  if not v:
    cf.append(idx)

ans = 0

for i in range(len(rf)):
  if rf[i] == -1:
    continue
  for j in range(len(cf)):
    if cf[j] == -1:
      continue
    if castle[rf[i]][cf[j]] == '.':
      ans +=1
      rf[i] = -1
      cf[j] = -1

print(ans)
print(rf)
print(cf)

for i in rf:
  if i != -1:
    ans += 1

for i in cf:
  if i != -1:
    ans += 1

print(ans)