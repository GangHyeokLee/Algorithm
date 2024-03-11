from collections import deque

n, m = map(int, input().split())

ground = []

start = []
for i in range(n):
  row = list(map(int, input().split()))
  if 2 in row:
    idx = row.index(2)
    start = [i, idx]
  for j in range(m):
    if row[j] == 1:
      row[j] = -1
  ground.append(row)

que = deque()

que.append(start)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ground[start[0]][start[1]] = 0

while que:
  x, y = que.popleft()
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m and ground[nx][ny] == -1:
      ground[nx][ny] = ground[x][y] + 1
      que.append([nx, ny])
      
for i in ground:
  for j in i:
    print(j, end=" ")
  print()