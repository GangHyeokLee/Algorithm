n = int(input())

que = []
que.append((n, 0))

idx = 0
visited = [True for i in range(n+1)]
visited[n] = False

while idx < len(que):
  now, count = que[idx]
  idx += 1
  
  if now == 1:
    print(count)
    break
  
  if now % 3 == 0 and visited[now // 3]:
    visited[now // 3] = False
    que.append((now // 3, count + 1))
  if now % 2 == 0 and visited[now // 2]:
    visited[now // 2] = False
    que.append((now // 2, count + 1))
  if visited[now - 1]:
    visited[now - 1] = False
    que.append((now - 1, count + 1))
