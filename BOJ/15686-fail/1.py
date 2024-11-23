from itertools import combinations

N, M = map(int, input().split())

houses = []
chickens = []

for i in range(N):
  tmp = input().split()
  for j in range(N):
    if tmp[j] == '1':
      houses.append([i, j])
    elif tmp[j] == '2':
      chickens.append([i, j])

temp = list(combinations(chickens, M))

ans = 1000 * 2 * N
for i in temp:
  local_ans = 0
  for h in houses:
    h_min = 1000
    for c in i:
      h_min = min(h_min, abs(c[0] - h[0]) + abs(c[1] - h[1]))
    local_ans += h_min
  ans = min(ans, local_ans)

print(ans)