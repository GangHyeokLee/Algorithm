import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

def bfs(mid):
  que = deque([fs])
  visited = [False] * (n+1)
  visited[fs] = True

  while que:
    x = que.popleft()
    for y, weight in adj[x]:
      if not visited[y] and weight >= mid:
        visited[y] = True
        que.append(y)
  
  return visited[fe]

start = 100000000
end = 1

for _ in range(m):
  x, y, weight = map(int, input().split())
  adj[x].append((y, weight))
  adj[y].append((x, weight))
  start = min(start, weight)
  end = max(end, weight)

fs, fe = map(int, input().split())

result = start
while(start <= end):
  mid = (start + end) // 2
  if bfs(mid):
    result = mid
    start = mid+1
  else:
    end = mid - 1

print(result)