import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

maze = [list(input().strip()) for _ in range(n)]

cost = [list(map(int, input().split())) for _ in range(n)]

visited = [[True] * m for _ in range(n)] # 방문 안 했으면 N, 탈출할 수 있으면 O, 사이클이면 C


def findNext(y, x):
  dir = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D":[1, 0]}
  dy, dx = dir[maze[y][x]]
  return [y + dy, x + dx]

stack = []

answer = 0

def dfs(y, x):
  global answer
  
  ny, nx = findNext(y, x)
  
  if 0 <= ny < n and 0 <= nx < m:
    if visited[ny][nx]:
      visited[ny][nx] = False
      stack.append((ny, nx))
      dfs(ny, nx)
      stack.pop()
    else:
      minCost = 1000
      idx = len(stack) - 1
      
      # 방문 했다면 stack을 거꾸로 돌면서 minCost 계산, 만약 탈출가능이라면 idx가 -1일 것이고 사이클이라면 idx >= 0인 상태에서 stack[idx] == (ny, nx)일 것
      while idx >= 0 and stack[idx] != (ny, nx):
        i, j = stack[idx]
        minCost = min(minCost, cost[i][j])
        idx -= 1
    
      # 그래서 사이클로 판명되면 
      if idx >= 0 and stack[idx] == (ny, nx):
        answer += min(minCost, cost[ny][nx])

for i in range(n):
  for j in range(m):
    if visited[i][j]:
      stack.append((i, j))
      dfs(i, j)
      stack.pop()

print(answer)