import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())

eg = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  eg[a].append(b)
  eg[b].append(a)
for e in eg:
  e.sort(reverse=True)
visited = [0 for _ in range(n+1)]
cnt = 2
def dfs(start):
  global cnt
  for e in eg[start]:
    if visited[e] == 0:
      visited[e] = cnt
      cnt += 1
      dfs(e)
visited[r] = 1
dfs(r)
for i in range(1, n+1):
  print(visited[i])