r, c = map(int, input().split())

board = [input() for _ in range(r)]

que = [(0, 0)]
visited = {}

idx = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while idx < len(que):
  y, x = que[idx]
  idx += 1
  
  visited[board[y][x]] = True
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    
    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in visited:
      que.append((ny, nx))
print(idx - 1)