import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ocean = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(visited):
  count = 0
  for i in range(n):
    for j in range(m):
      if ocean[i][j] and visited[i][j]:
        count += 1
        que = [(i, j)]
        visited[i][j] = False
        idx = 0
        touching = []
        while idx < len(que):
          y, x = que[idx]
          idx += 1
          touch = 0
          for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx]:
              if ocean[ny][nx] > 0:
                que.append((ny, nx))
                visited[ny][nx] = False
              else:
                touch += 1
          touching.append(touch)
        
        for k in range(idx):
          y, x = que[k]
          ocean[y][x] = max(ocean[y][x] - touching[k], 0)
  return count
time = 0
while True:
  time += 1
  visited = [[True] * m for _ in range(n)]
  count = bfs(visited)
  
  if count >= 2:
    print(time - 1)
    break
  elif count == 0:
    print(0)
    break