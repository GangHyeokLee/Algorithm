import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]
visited = [[True] * m for _ in range(n)]

def findNext(y, x, maze):
  dir = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D":[1, 0]}
  dy, dx = dir[maze[y][x]]
  return [y + dy, x + dx]

ans = 0

for i in range(n):
  for j in range(m):
    if visited[i][j]:
      que = [(i, j)]
      idx = 0
      visited[i][j] = False
      
      while idx < len(que):
        y, x = que[idx]
        idx += 1
        ny, nx = findNext(y, x, maze)
        
        if 0 <= ny < n and 0 <= nx < m:
          if visited[ny][nx]:
            que.append((ny, nx))
            visited[ny][nx] = False
          else:
            ci = idx - 1
            minCost = cost[ny][nx]
            while ci >= 0 and que[ci] != (ny, nx):
              cy, cx = que[ci]
              minCost = min(minCost, cost[cy][cx])
              ci -= 1
            
            if ci >= 0 and que[ci] == (ny, nx):
              ans += minCost

print(ans)