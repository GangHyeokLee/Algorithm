n = int(input())

city = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

# BFS인데 비가 1부터 100까지 왔을 때 각각의 안전한 영역 찾기인가?

def bfs(h, visited):
  safeZone = 0
  for i in range(n):
    for j in range(n):
      if city[i][j] > h and visited[i][j]:
        visited[i][j] = False
        
        que = [(i, j)]
        idx = 0
        
        while idx < len(que):
          y, x = que[idx]
          idx += 1
          for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and city[ny][nx] > h and visited[ny][nx]:
              visited[ny][nx] = False
              que.append((ny, nx))
        
        safeZone += 1
  return safeZone

ans = 0
for i in range(101):
  visited = [[True] * (n) for _ in range(n)]
  safeZone = bfs(i, visited)
  
  if safeZone == 0: # 최대높이보다 커졌다.
    break
  
  ans = max(ans, safeZone)
print(ans)