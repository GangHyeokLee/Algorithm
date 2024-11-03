from collections import defaultdict

n, m = map(int, input().split())

tree = defaultdict(list)

for _ in range(n-1):
  a, b, c = map(int, input().split())
  
  tree[a].append((b, c))
  tree[b].append((a, c))
for _ in range(m):
  a, b = map(int, input().split())
  que = [(a, 0)]
  idx = 0
  visited = [True] * (n+1)
  visited[a] = False
  
  ans = []
  
  while idx < len(que):
    now, cost = que[idx]
    idx += 1
    
    if now == b:
      ans.append(cost)
    
    for next, c in tree[now]:
      if visited[next]:
        que.append((next, cost + c))
        visited[next] = False
  print(min(ans))