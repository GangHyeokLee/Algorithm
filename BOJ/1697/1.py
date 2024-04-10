from collections import deque

n, k = map(int, input().split())

que = deque()

que.append((n, 0))
visited = [True] * 100001

while que:
  (now, time) = que.popleft()
  
  if now == k:
    print(time)
    break
  
  if now - 1 >= 0 and visited[now-1]:
    visited[now-1] = False
    que.append((now-1, time+1))
  if now + 1 <= 100000 and visited[now+1]:
    visited[now+1] = False
    que.append((now + 1, time+1))
  
  if now * 2 <= 100000 and visited[2 * now]:
    visited[2 * now] = False
    que.append((2 * now, time+1))