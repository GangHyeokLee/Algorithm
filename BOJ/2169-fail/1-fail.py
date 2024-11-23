import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

mars = list(list(map(int, input().split())) for _ in range(n))

dp = [[-1000] * m for _ in range(n)]

dp[0][0] = mars[0][0]
for i in range(1, n):
    dp[0][i] = mars[0][i] + dp[0][i - 1]

# 점화식
# dp[y][x] = mars[y][x] + max(dp[y-1][x], dp[y][x+1], dp[y][x-1])

dy = [-1, 0, 0]
dx = [0, 1, -1]
visited = [[True] * m for _ in range(n)]

visited[-1][-1] = False


def dfs(sy, sx, visited, dp):
    if dp[sy][sx] != -1000:
        return dp[sy][sx]

    now = mars[sy][sx]

    next = -1000

    for d in range(3):
        ny = sy + dy[d]
        nx = sx + dx[d]

        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx]:
            visited[ny][nx] = False
            tmp = dp[ny][nx]
            next = max(next, dfs(ny, nx, visited, dp))
            visited[ny][nx] = True
            dp[ny][nx] =tmp

    dp[sy][sx] = max(dp[sy][sx], now + next)
    return dp[sy][sx]


print(dfs(n - 1, m - 1, visited, dp))
