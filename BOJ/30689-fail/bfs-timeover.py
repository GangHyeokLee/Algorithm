import sys

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(input().strip()) for _ in range(n)]

cost = [list(map(int, input().split())) for _ in range(n)]

visited = [["N"] * m for _ in range(n)] # 방문 안 했으면 N, 탈출할 수 있으면 O, 사이클이면 C


def findNext(y, x, maze):
  dir = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D":[1, 0]}
  dy, dx = dir[maze[y][x]]
  return [y + dy, x + dx]

cycles = []

for i in range(n):
  for j in range(m):
    if visited[i][j] == "N":
      que = [(i, j)]
      idx = 0
      visited[i][j] = "O"
      
      v = set()
      v.add((i, j))
      
      cycle = False
      
      while idx < len(que):
        y, x = que[idx]
        idx += 1
        ny, nx = findNext(y, x, maze)
        
        if 0 <= ny < n and 0 <= nx < m:
          if visited[ny][nx] == "N" and (ny, nx) not in v:
            que.append((ny, nx))
            visited[ny][nx] = "O"
            v.add((ny, nx))
          elif (ny, nx) in v: # 탐색 중 사이클이 생김
            circle = [(ny, nx)]
            y, x = findNext(ny, nx, maze)
            while y != ny or x != nx:
              circle.append((y, x))
              y, x = findNext(y, x, maze)
            cycles.append(circle)
            cycle = True
            
          elif visited[ny][nx] == "C": # 사이클이 있는 코스랑 만남
            cycle = True
      
      if cycle:
        for y, x in que:
          visited[y][x] = "C"

ans = 0
for c in cycles:
  minCost = 1000
  for y, x in c:
    minCost = min(minCost, cost[y][x])
  ans += minCost
  
print(ans)