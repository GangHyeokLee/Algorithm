import sys

sys.setrecursionlimit(10 ** 6)

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < m and 0 <= ny < n and plant[ny][nx] == 1:
      plant[ny][nx] = 0
      dfs(nx, ny)

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
        dfs(j, i)
        ans += 1
        
  print(ans)