import math
from heapq import heappop, heappush

n = int(input())

start = []
for i in range(n):
  x, y = map(float, input().split())
  start.append((i, x, y))

adj = [[] for _ in range(n)]

for i in range(n):
  for j in range(n):
    distance = math.sqrt((start[i][2] - start[j][2])**2 + (start[i][1] - start[j][1])**2)
    adj[i].append((j, distance))

que = []
ans = 0

# cost, node
heappush(que, (0, 0))
visited = [True] * n

while que:
  cost, now = heappop(que)
  
  if visited[now]:
    visited[now] = False
    ans += cost
    for next, dist in adj[now]:
      if visited[next]:
        heappush(que, (dist, next))
print(ans)