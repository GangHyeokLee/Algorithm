n, m, b = map(int, input().split())

field = []

minh = 257
maxh = -1
for i in range(n):
  field.append(list(map(int, input().split())))
  minh = min([minh,min(field[i])])
  maxh = max([maxh, max(field[i])])

ans = []
for h in range(minh, maxh+1):
  rest = b
  time = 0
  minus = False
  for i in range(n):
    for j in range(m):
      dif = field[i][j] - h
      if dif > 0:
        rest += dif
        time += 2 * dif
      elif dif < 0:
        rest += dif
        if rest < 0:
          minus = True
          break
        time -= dif
    if minus:
      break
  if not minus:
    ans.append((time, h))
    
ans.sort()

mintime = ans[0][0]
maxh = 0

for i in ans:
  if i[0] == mintime:
    maxh = max([maxh, i[1]])
    
print(mintime, maxh)