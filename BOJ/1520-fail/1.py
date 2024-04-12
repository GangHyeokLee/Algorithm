n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, -1, 0]
dx = [1, 0, 0, -1]

ans = 0
# 특정 점까지 도달할 수 있는 경우의 수 기록용
memo = [[-1] * m for _ in range(n)]
memo[n-1][m-1] = 1

def dfs(y, x):
  if memo[y][x] != -1:
    return memo[y][x]

  memo[y][x] += 1
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] < maps[y][x]:
      memo[y][x] += dfs(ny, nx)
  return memo[y][x]

print(dfs(0, 0))