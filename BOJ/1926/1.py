n, m = map(int, input().split())

paint = [list(map(int, input().split())) for _ in range(n)]

# bfs로 풀기

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = []
for i in range(n):
  for j in range(m):
    # 1을 찾는 순간 탐색 시작
    if paint[i][j]:
      que = []
      que.append((i, j))
      idx = 0
      
      # 방문한 표시
      paint[i][j] = 0
      
      while idx < len(que):
        y, x = que[idx]
        idx += 1

        for d in range(4):
          ny = y + dy[d]
          nx = x + dx[d]
          
          if 0 <= ny < n and 0 <= nx < m and paint[ny][nx]:
            que.append((ny, nx))
            # 방문했다고 표시하기
            paint[ny][nx] = 0
            
      # idx의 값 혹은 que의 길이가 연결된 그림의 넓이
      ans.append(idx)
      
print(len(ans))
print(max(ans) if ans else 0)