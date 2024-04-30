dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for _ in range(int(input())):
  n, m, k = map(int, input().split())
  
  bat = [[0] * m for _ in range(n)]
  for _ in range(k):
    y, x = map(int, input().split())
    
    bat[y][x] = 1
  count = 0
  for i in range(n):
    for j in range(m):
      if bat[i][j]:
        count += 1
        que = [(i, j)]
        bat[i][j] = 0
        idx =  0
        while idx < len(que):
          y, x = que[idx]
          idx += 1
          
          for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and bat[ny][nx]:
              bat[ny][nx] = 0
              que.append((ny, nx))
  print(count)