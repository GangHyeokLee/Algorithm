from heapq import heappop, heappush

import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  edges[a].append((b, 1))
  

dist = [2*n] * (n+1)

dist[x] = 0

q = [(0, x)]

while q:
  cost, idx = heappop(q)
  
  if dist[idx] < cost:
    continue
  
  
  
  for adj, d in edges[idx]:
    if dist[adj] > cost + d:
      dist[adj] = cost + d
      heappush(q, (dist[adj], adj))

ans = []
for d in range(n+1):
  if dist[d] == k :
    ans.append(d)

if ans:
  for i in ans:
    print(i)
else:
  print(-1)