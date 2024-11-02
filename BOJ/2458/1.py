from collections import defaultdict

n, m = map(int, input().split())

h = defaultdict(list)
H = defaultdict(list)

for _ in range(m):
  a, b = map(int, input().split())
  
  h[a].append(b)
  H[b].append(a)
  
ans = 0
for i in range(1, n+1):
  que = [i]
  idx = 0
  visited = [True] * (n+1)
  visited[i] = False
  
  while idx <len(que):
    now = que[idx]
    idx += 1
    
    for next in h[now]:
      if visited[next]:
        visited[next] = False
        que.append(next)
  rank = len(que) - 1
  
  que = [i]
  idx = 0
  visited = [True] * (n+1)
  visited[i] = False
  
  while idx < len(que):
    now = que[idx]
    idx += 1
    
    for next in H[now]:
      if visited[next]:
        visited[next] = False
        que.append(next)
  rank += len(que)

  if rank == n:
    ans += 1
    
print(ans)