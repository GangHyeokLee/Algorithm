n = int(input())

weight = []
height = []

for i in range(n):
  w, h = map(int, input().split())
  
  weight.append((w, i))
  height.append((h, i))
  
weight.sort(reverse=True)
height.sort(reverse=True)

rank = [[] for i in range(n)]

for i in range(n):
  rank[weight[i][1]].append(i)
  rank[height[i][1]].append(i)

for i in range(n):
  rank[i].sort()
  rank[i].append(i)

rank.sort()

print(rank)
r = 1
next = 0
for i in range(n):
  l = 0
  if i < next:
    continue
  cut = False
  rank[i].append(r)
  for j in range(i+1, n):
    if rank[i][0] < rank[j][0] and rank[i][1] < rank[j][1]:
      next = j
      l = j - i
      cut = True
      break
    else:
      rank[j].append(r)
  if cut:
    r += l
    continue

ans = [-1] * n

for i in rank:
  ans[i[-2]] = i[-1]
  
print(ans)