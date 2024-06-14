n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

visited = [[0] * m for _ in range(n)]

visited[n-1][m-1] = 1

def dfs(start):
  y, x = start
  
  if visited[y][x] == 0:
    return visited[y][x]
  
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    
    if 0 <= ny < n and 0 <= nx < m and map[y][x] > map[ny][nx]:
      visited[y][x] += dfs((ny, nx))
  
  return visited[y][x]

print(dfs((0, 0)))