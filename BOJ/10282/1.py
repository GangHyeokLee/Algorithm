from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n, d, c = map(int, input().split())
  
  adj = [[] for _ in range(n+1)]
  
  for _ in range(d):
    a, b, cost = map(int, input().split())
    
    adj[b].append((a, cost))
  
  # 다익스트라
  que = []
  heappush(que, (0, c))
  dist = [1000 * n] * (n+1)
  dist[c] = 0
  
  while que:
    cost, now = heappop(que)
    
    if dist[now] < cost:
      continue
    
    for next, d in adj[now]:
      if dist[next] > cost + d:
        dist[next] = cost + d
        heappush(que, (dist[next], next))
  ans = 0
  cnt = 0
  for d in dist:
    if d < 1000 * n:
      cnt += 1
      ans = max(ans, d)
  print(cnt, ans)