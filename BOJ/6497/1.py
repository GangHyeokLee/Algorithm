import sys
from heapq import heappop, heappush
input = sys.stdin.readline

m, n = map(int, input().split())

while m!=0 and n!=0:
  adj = [[] for _ in range(m)]
  total = 0
  road = []
  for _ in range(n):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
    total += c
  que = []
  # 시작점
  heappush(que, (0, 0))
  visited = [True] * m

  ans = 0
  while que:
    cost, house = heappop(que)
    
    # 방문하지 않은 집
    if visited[house]:
      ans += cost
      visited[house] = False
      
      for h in adj[house]:
        if visited[h[1]]:
          heappush(que, h)

  print(total - ans)
  m, n = map(int, input().split())