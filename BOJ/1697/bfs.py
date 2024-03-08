from collections import deque

n, k = map(int, input().split())

queue = deque()

queue.append([n, 0])

visited = [True] * 100001

while queue:
  now, time = queue.popleft()
  visited[now] = False
  
  if now == k:
    print(time)
    break
  
  if now < 100000 and visited[now+1]:
    queue.append([now+1, time+1])
  if 2 * now <= 100000 and visited[2 * now]:
    queue.append([2 * now, time+1])
  if now > 0 and visited[now - 1]:
    queue.append([now - 1, time + 1])