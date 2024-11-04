from heapq import heappush, heappop

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
count = 1
while True:
  n = int(input())
  
  if n == 0:
    break
  cave = list(list(map(int, input().split())) for _ in range(n))
  dist = [[n * n * 100] * n for _ in range(n)]
  
  dist[0][0] = cave[0][0]
  
  q = [(dist[0][0], 0, 0)]
  
  while q:
    cost, y, x = heappop(q)
    
    if dist[y][x] < cost:
      continue
    
    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]
      
      if 0 <= ny < n and 0 <= nx < n and dist[ny][nx] > cost + cave[ny][nx]:
        dist[ny][nx] = cost + cave[ny][nx]
        heappush(q, (dist[ny][nx], ny, nx))
        
  print('Problem '+str(count)+ ":",  dist[-1][-1])
  count += 1