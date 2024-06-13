from collections import defaultdict

n, m, v = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, (n+1)):
  graph[i].sort()

log = []
def dfs(start, visited):
  global log
  log.append(start)
  for next in graph[start]:
    if visited[next]:
      visited[next] = False
      dfs(next, visited)
      # visited[next] = True
visited = [True] * (n+1)
visited[v] = False
dfs(v, visited)

print(' '.join(map(str, log)))


log.clear()
idx = 0
log.append(v)
visited = [True] * (n+1)
visited[v] = False
while idx < len(log):
  now = log[idx]
  idx += 1
  
  for next in graph[now]:
    if visited[next]:
      visited[next] = False
      log.append(next)
      
print(' '.join(map(str, log)))
