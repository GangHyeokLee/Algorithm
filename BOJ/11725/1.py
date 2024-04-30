import sys
input = sys.stdin.readline

n = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b = map(int, input().split())
  
  adj[a].append(b)
  adj[b].append(a)
  

parent = [i for i in range(n+1)]
visited = [True] * (n+1)

que = [1]
visited[0] = False
visited[1] = False
idx = 0

while idx < len(que):
  now = que[idx]
  idx += 1
  
  for child in adj[now]:
    if visited[child]:
      visited[child] = False
      que.append(child)
      parent[child] = now

for i in range(2, n+1):
  print(parent[i])