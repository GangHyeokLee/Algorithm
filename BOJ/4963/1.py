dy = [0, 0, 1, -1, 1, 1, -1, -1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]

while True:
  m, n = map(int, input().split())
  
  if m == 0 and n == 0:
    break
  
  grid = [list(map(int, input().split())) for _ in range(n)]
  count = 0
  for i in range(n):
    for j in range(m):
      if grid[i][j]:
        count += 1
        que = [(i, j)]
        idx = 0
        grid[i][j] = 0
        while idx < len(que):
          y, x = que[idx]
          idx += 1
          
          for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and grid[ny][nx]:
              grid[ny][nx] = 0
              que.append((ny, nx))
  
  print(count)