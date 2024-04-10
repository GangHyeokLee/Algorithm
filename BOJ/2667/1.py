n = int(input())
apart = [input() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[True] * n for _ in range(n)]

# que 길이 담을 리스트
ans = []
for i in range(n):
  for j in range(n):
    # 전체 돌면서 1 나오는 순간 탐색시작, BFS
    if apart[i][j] == '1' and visited[i][j]:
      que = []
      idx = 0
      que.append([i, j])
      visited[i][j] = False
      while idx < len(que):
        [y, x] = que[idx]
        idx += 1
        for d in range(4):
          ny = y + dy[d]
          nx = x + dx[d]
          if 0 <= ny < n and 0 <= nx < n and apart[ny][nx] == '1' and visited[ny][nx]:
            visited[ny][nx] = False
            que.append([ny, nx])
      ans.append(idx)
      
print(len(ans))
ans.sort()
for i in ans:
  print(i)