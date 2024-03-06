from collections import deque

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  queue = deque()
  queue.append([x, y])
  while len(queue) > 0:
    t = queue.popleft()
    for i in range(4):
      nx = t[0] + dx[i]
      ny = t[1] + dy[i]
      
      if 0 <= nx < m and 0 <= ny < n and plant[ny][nx] == 1:
        plant[ny][nx] = 0
        queue.append([nx, ny])

for _ in range(t):
  m, n, k = map(int, input().split())
  plant = []
  ans = 0
  for i in range(n):
    plant.append([0] * m)
  for _ in range(k):
    x, y = map(int, input().split())
    plant[y][x] = 1
  
  for i in range(n):
    for j in range(m):
      if plant[i][j] == 1:
        plant[i][j] = 0
        bfs(j, i)
        ans += 1
        
  print(ans)