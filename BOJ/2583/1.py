n, m, k = map(int, input().split())

lectang = [list(map(int, input().split())) for _ in range(k)]

paper = [[1] * m for _ in range(n)]

for l in lectang:
  for i in range(l[1], l[3]):
    for j in range(l[0], l[2]):
      paper[i][j] = 0

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

ans = []
for i in range(n):
  for j in range(m):
    if paper[i][j] == 1:
      que = [(i, j)]
      idx = 0
      
      paper[i][j] = 0
      while idx < len(que):
        y, x = que[idx]
        idx += 1
        
        for d in range(4):
          ny = y + dy[d]
          nx = x + dx[d]
          
          if 0 <= ny < n and 0 <= nx < m and paper[ny][nx]:
            paper[ny][nx] = 0
            que.append((ny, nx))
            
      ans.append(idx)
      
print(len(ans))
ans.sort()

print(' '.join(map(str, ans)))