import sys
input = sys.stdin.readline

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

que = []
idx = 0

riped = []

# 익은 거 찾아서 시간 넣기
for i in range(n):
  for j in range(m):
    if box[i][j] == 1:
      que.append((i, j, 0))
      box[i][j] = -1
      

# BFS
while idx < len(que):
  y, x, t = que[idx]
  idx += 1
  
  for d in range(4):
    ny = y + dy[d]
    nx = x + dx[d]
    
    # 방문한 칸은 -1로 처리
    if 0 <= ny < n and 0 <= nx < m and box[ny][nx] == 0:
      box[ny][nx] = -1
      que.append((ny, nx, t+1))

# 모든 칸에 있는 값 다 더해서 다 익었는지 판별
ans = 0
for i in box:
  ans += sum(i)

if ans != -n*m:
  print(-1)
else:
  print(que[-1][-1])