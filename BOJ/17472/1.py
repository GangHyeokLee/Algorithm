from heapq import heappop, heappush

n, m = map(int, input().split())

island = [list(map(int, input().split())) for _ in range(n)]

# 섬 찾기 bfs

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

boundary = []

for i in range(n):
  for j in range(m):
    if island[i][j]:
      # 각 섬의 최대 최소 x, y값을 얻기 위해 큐 따로 유지
      quex = []
      quey = []
      que = []
      quex.append(j)
      quey.append(i)
      que.append((i, j))
      island[i][j] = 0
      idx = 0
      while idx < len(que):
        y, x = quey[idx], quex[idx]
        idx += 1
        
        for d in range(4):
          ny = y + dy[d]
          nx = x + dx[d]
          if 0 <= ny < n and 0 <= nx < m and island[ny][nx]:
            quex.append(nx)
            quey.append(ny)
            que.append((ny, nx))
            island[ny][nx] = 0
      boundary.append((len(boundary), (min(quey),max(quey)), (min(quex), max(quex)), que))
      print(boundary[-1])
      
adj = [[] for _ in range(n)]

for i in boundary:
  for j in boundary:
    # 섬 사이의 거리 구하기
    idi, xi, yi, qi = i
    idj, xj, yj, qj = j
    cost = 0
    # 가로로 겹치는지 세로로 겹치는 지 확인
    # 가로로 걸침
    if xi[0] <= xj[0] <= xi[1] or xi[0] <= xj[1] <= xi[1] or xj[0] <= xi[0] <= xj[1] or xj[0] <= xi[1] <= xj[1]:
      cost = min(abs(yj[0] - yi[1]), abs(yj[1]-yi[0])) - 1
    elif yi[0] <= yj[0] <= yi[1] or yi[0] <= yj[1] <= yi[1] or yj[0] <= yi[0] <= yj[1] or yj[0] <= yi[1] <= yj[1]:
      cost = min(abs(xj[0] - xi[1]), abs(xj[1]-xi[0])) - 1
    # 다리 최소 길이 2이거나 자기 자신 가리키면
    if idi==idj or cost < 2:
        cost = n + m
    adj[idi].append((cost, idj))
  print(idi, adj[idi])
  
# 프림
heap = []
heappush(heap, (0, 0))
visited = [True] * n

ans = 0
while heap:
  cost, now = heappop(heap)
  
  if visited[now] and cost < n+m:
    ans += cost
    visited[now] = False
    
    for next in adj[now]:
      if visited[next[1]]:
        heappush(heap, next)

print(ans)