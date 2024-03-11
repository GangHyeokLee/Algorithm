from collections import deque

m, n = map(int, input().split())

bat = []
que = deque()

for i in range(n):
  row = list(map(int, input().split()))
  
  for j in range(m):
    if row[j] == 1:
      que.append((i, j, 0))
  
  bat.append(row)
  

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

time = []

while que:
  now = que.popleft()
  time.append(now[2])
  
  for i in range(4):
    nx = now[0] + dx[i]
    ny = now[1] + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m and bat[nx][ny] == 0:
      bat[nx][ny] = 1
      que.append((nx, ny, now[2]+1))
      
done = True  
for i in range(n):
  if 0 in bat[i]:
    done = False
    
if done:
  print(max(time))
else:
  print(-1)