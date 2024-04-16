# 치즈 문제랑 비슷할 줄 알앗느데 아니었따.
# 그냥 빙산 있는 리스트 두 개 둔 다음에 BFS 돌면서 연산 결과 왔다 갔다 하면서 저장하기

n, m = map(int, input().split())

sea1 = [list(map(int, input().split())) for _ in range(n)]

sea2 = [[0] * m for _ in range(n)]

sea12 = [sea1, sea2]

dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
sidx = 0

time = 0
while True:
  iceberg = []
  sea = sea12[sidx]
  visited = [[True] * m for _ in range(n)]
  for i in range(n):
    for j in range(m):
      if sea[i][j]:
        que = []
        idx = 0
        que.append((i, j))
        visited[i][j] = False
        
        while idx < len(que):
          y, x = que[idx]
          idx += 1
          height = sea[y][x]
          
          for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            
            if 0 <= ny < n and 0 <= nx < m:
              if sea[ny][nx] and visited[ny][nx]:
                visited[ny][nx] = False
                que.append((ny, nx))
              # 바다 닿는 수 만킄 1 빼기
              else:
                height -= 1
          # 다른 바다에 저장
          sea12[abs(sidx-1)][y][x] = height
        iceberg.append(que)
        print(iceberg, time)
      # 나머지 부분 갱신하기
      else:
        sea12[abs(sidx-1)][i][j] = sea[i][j]
  if len(iceberg) == 0:
    print(0, 0)
    break
  elif len(iceberg) >= 2:
    print(iceberg)
    print(len(iceberg), time)
    break
  sidx = abs(sidx-1)
  time += 1
  iceberg.clear()
  