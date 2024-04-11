n, m, k = map(int, input().split())

aisle = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
  r, c = map(int, input().split())
  
  aisle[r][c] = 1
  
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

ans = 0

for i in range(1,n+1):
  for j in range(1, m+1):
    if aisle[i][j]:
      aisle[i][j] = 0
      que = []
      que.append((i, j))
      idx = 0
      while idx < len(que):
        y, x = que[idx]
        idx += 1
        
        for d in range(4):
          ny = y + dy[d]
          nx = x + dx[d]
          
          if 0 <= ny <= n and 0 <= nx <= m and aisle[ny][nx]:
            que.append((ny, nx))
            aisle[ny][nx] = 0
      # idx가 음식물 그룹의 크기가 됨
      ans = max(ans, idx)
      
print(ans)