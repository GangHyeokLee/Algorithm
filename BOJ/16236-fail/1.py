import sys
from heapq import *
input = sys.stdin.readline

n = int(input())

space = []
shark = []
for i in range(n):
  row = list(map(int, input().split()))
  for j in range(n):
    if row[j] == 9:
      # 상어 위치
      shark = [i, j]
  space.append(row)
# 먹을 수 있는 물고기 사라질 때까지 BFS 돌기

visited = [[True] * n for _ in range(n)]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

def bfs(y, x, size):
  # 거리 겸 방문 기록
  visited = [[-1] * n for _ in range(n)]
  visited[y][x] = 0
  # 먹은 물고기 좌표와 거리
  eaten = []
  
  que = [(y, x)]
  idx = 0
  
  while idx < len(que):
    y, x = que[idx]
    idx += 1
    for d in range(4):
      ny = y + dy[d]
      nx = x + dx[d]
      if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == -1 and space[ny][nx] <= size:
        que.append((ny, nx))
        visited[ny][nx] = visited[y][x] + 1
        if space[ny][nx] and space[ny][nx] < size:
          eaten.append((visited[ny][nx], ny, nx))
  return eaten
# 먹은 횟수 저장
eatcount = 0
size = 2
time = 0
while True:
  space[shark[0]][shark[1]] = 0 #기존 위치 날림
  eaten = bfs(shark[0], shark[1], size)
  
  # 물고기 하나도 못 먹음
  if len(eaten) == 0:
    break
  
  # 거리, 행번호, 열번호 순으로 정렬
  eaten.sort()
  d, ny, nx = eaten[0]
  shark = [ny, nx] #상어 이동함
  time += d
  eatcount += 1
  
  # 상어 성장
  if eatcount == size:
    size += 1
    eatcount = 0
  
print(time)