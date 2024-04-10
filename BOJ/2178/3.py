# 최단거리 -> BFS
n, m = map(int, input().split())
maze = [input() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = []
que.append([0, 0, 1])
visited = [[True] * m for _ in range(n)]
idx = 0

while idx < len(que):
  [y, x, count] = que[idx]
  idx += 1
  
  if y == n-1 and x == m-1:
    print(count)
    break
  
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]    
    if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == '1' and visited[ny][nx]:
      que.append([ny, nx, count+1])
      visited[ny][nx] = False