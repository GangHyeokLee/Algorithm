from collections import deque

omok = [list(map(int, input().split())) for _ in range(19)]

dx = [1, 0, 1, 1, -1, 0, -1, -1] 
dy = [0, 1, 1, -1, 0, -1, -1, 1] # 우 상 우하 우상 좌 하 좌상 좌하

found = False

for i in range(19):
  for j in range(19):
    if not found and omok[i][j]:
      que = deque()
      que.append((i, j, 1, 4)) #좌표, 개수, 방향
      ans = [[(i, j)] for _ in range(4)] # 방향 별 개수, 좌우, 상하, 우상좌하, 좌상우하
      visited = [[True] * 19 for _ in range(19)]
      visited[i][j] = False
      while que:
        (y, x, count, dir) = que.popleft()
        if dir != 4:
          ans[dir].append((y, x))
        for d in range(8):
          ny = y + dy[d]
          nx = x + dx[d]
          if 0 <= ny < 19 and 0 <= nx < 19 and visited[ny][nx] and omok[ny][nx] == omok[i][j] and (dir == 4 or d%4 == dir):
            visited[ny][nx] = False
            que.append((ny, nx, count + 1 if dir==4 or d%4 == dir else count, d%4))
      for dir, a in enumerate(ans):
        if len(a) == 5:
          a.sort()
          print(omok[i][j])
          if dir < 3:
            print(a[0][0] + 1, a[0][1] + 1)
          else:
            print(a[-1][0] + 1, a[-1][1] + 1)
          found = True
          break
  if found:
    break
if not found:
  print(0)