dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(int(input())):
  n = int(input())
  start = list(map(int, input().split()))
  start.append(0)
  end = tuple(map(int, input().split()))
  
  que = [start]
  idx = 0
  
  visited = [[True] * n for _ in range(n)]
  visited[start[0]][start[1]] = False
  
  while idx < len(que):
    y, x, count = que[idx]
    idx += 1
    
    if y == end[0] and x == end[1]:
      print(count)
      break
    
    for d in range(8):
      ny = y + dy[d]
      nx = x + dx[d]
      
      if 0 <= ny < n and 0 <= nx < n and visited[ny][nx]:
        visited[ny][nx] = False
        que.append((ny, nx, count+1))