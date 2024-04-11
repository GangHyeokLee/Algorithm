import sys

input = sys.stdin.readline

r, c = map(int, input().strip().split())
board = [list(input().strip()) for _ in range(r)]
visited = set()

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

ans = 0

def dfs(y, x, count):
  global ans
  ans = max(ans, count)
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    
    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] not in visited:
      visited.add(board[ny][nx])
      dfs(ny, nx, count + 1)
      visited.remove(board[ny][nx])

visited.add(board[0][0])
dfs(0, 0, 1)
print(ans)