from collections import defaultdict

n = int(input())
x, y = map(int, input().split())

parent = defaultdict(list)

for _ in range(int(input())):
  p, c = map(int, input().split())
  
  parent[p].append(c)
  parent[c].append(p)
  

que = [(x, 0)]

idx = 0
found = False
visited = [True] * (n+1)
visited[x] = False

while idx < len(que):
  now, count = que[idx]
  idx += 1
  
  if now == y:
    found = True
    break
  
  for next in parent[now]:
    if visited[next]:
      visited[next] = False
      que.append((next, count+1))
      
if found:
  print(que[idx-1][1])
else:
  print(-1)