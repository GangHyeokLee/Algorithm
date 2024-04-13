n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

cheese = []

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

time = 0
while True:
  visited = [[True] * m for _ in range(n)]
  que = [(0, 0)]
  visited[0][0] = 1
  idx = 0
  while idx < len(que):
    y, x = que[idx]
    idx += 1
    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]
      # 방문하지 않은 점에 대해서 치즈랑 공기 찾기
      if 0 <= ny < n and 0 <= nx < m and visited[ny][nx]:
        # 치즈 일적에는 공기랑 닿은 면만 더하고 안 넣음
        # 치즈에 갇힌 공기는 큐에 들어갈 기회가 없어진다.
        if paper[ny][nx] >= 1:
          paper[ny][nx] += 1
        # 공기면 다음 탐색을 위해 큐에 넣음
        else:
          visited[ny][nx] = False
          que.append((ny, nx))
          
  
  for p in paper:
    print(p)
  print()
  
  melted = False
  for i in range(n):
    for j in range(m):
      if paper[i][j] >= 3:
        paper[i][j] = 0
        melted = True
      elif paper[i][j] == 2:
        paper[i][j] = 1
  if melted:
    time += 1
  else:
    break
  
print(time)
      
  