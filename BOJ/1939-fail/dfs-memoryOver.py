import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

def dfs(start, target, weight):
  if start == target:
    ans.append(min(weight))
    return
  
  for i in range(1, n+1):
    if island[start][i] > 0 and visited[i]:
      weight.append(island[start][i])
      visited[i] = False
      dfs(i, target, weight)
      weight.pop()
      visited[i] = True



bridge = []
ans = []

island = [[0] * (n+1) for i in range(n+1)]
print(island)

visited = [True] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())

  island[a][b] = max(c, island[a][b])
  island[b][a] = island[a][b]

fa, fc = map(int, input().split())

dfs(fa, fc, [])

print(max(ans))