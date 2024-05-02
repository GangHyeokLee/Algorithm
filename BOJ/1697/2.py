from collections import deque

n, k = map(int, input().split())

que = deque()
que.append((n, 0))
visited = [True] * 200001
visited[n] = False

while que:
  now, t = que.popleft()
  
  if now == k:
    print(t)
    break
  
  minus = now - 1
  if 0 <= minus and visited[minus]:
    que.append((minus, t+1))
    visited[minus] = False
  
  plus = now + 1
  if plus < 200001 and visited[plus]:
    que.append((plus, t+1))
    visited[plus] = False
    
  two = now * 2
  if two < 200001 and visited[two]:
    que.append((two, t+1))
    visited[two] = False
    