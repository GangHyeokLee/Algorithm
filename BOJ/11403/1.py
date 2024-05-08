n = int(input())

adj = [list(map(int, input().split())) for _ in range(n)]

ans = [[0] * n for _ in range(n)]
for i in range(n):
  que = [i]
  idx = 0
  
  visited = [[0] * n for _ in range(n)]
  while idx < len(que):
    now = que[idx]
    idx += 1
    
    for next in range(n):
      if adj[now][next] and visited[now][next] == 0:
        que.append(next)
        ans[now][next] = visited[now][next] = 1
        
  for q in range(1, len(que)):
    ans[i][que[q]] = 1

for r in ans:
  print(" ".join(map(str, r)))