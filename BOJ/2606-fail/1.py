from collections import deque

n = int(input())
m = int(input())

adj = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  
  adj[a][b] = 1
  adj[b][a] = 1
  
que = deque()

que.append(1)

visited = [False] * (n+1)
visited[1] = True

ans = 0
while que:
  now = que.popleft()
  
  for i in range(1, n+1):
    if adj[now][i] != 0 and not visited[i]:
      que.append(i)
      visited[i] = True
      ans += 1
      
print(ans)