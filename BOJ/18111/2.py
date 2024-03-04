n, m, b = map(int, input().split())

field = [0] * 257

for i in range(n):
  for i in list(map(int, input().split())):
    field[i] += 1

minh = -1
for i in range(257):
  if field[i] != 0:
    minh = i
    break

maxh = -1
for i in range(256, -1, -1):
  if field[i] != 0:
    maxh = i
    break

ans = []
for h in range(minh, maxh+1):
  rest = b
  time = 0
  for i in range(minh, maxh+1):
    if field[i] == 0:
      continue
    dif = i - h
    if dif > 0:
      rest += dif * field[i]
      time += 2 * dif * field[i]
    elif dif < 0:
      rest += dif * field[i]
      time -= dif * field[i]
  if rest < 0:
    continue
  ans.append((time, h))
  
ans.sort()

mintime = ans[0][0]

for i in range(len(ans)-1, -1, -1):
  if ans[i][0] == mintime:
    print(mintime, ans[i][1])
    break