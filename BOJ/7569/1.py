import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

dy = [0, 0, 1, -1, 0, 0]
dx = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

store = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

riped = []

for i in range(h):
  for j in range(n):
    for k in range(m):
      if store[i][j][k] == 1:
        riped.append((i, j, k, 0))
        store[i][j][k] = -1
if riped:
  idx = 0
  while idx < len(riped):
    z, y, x, t = riped[idx]
    idx += 1
    
    for d in range(6):
      nz = z + dz[d]
      ny = y + dy[d]
      nx = x + dx[d]
      
      if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and store[nz][ny][nx] == 0:
        store[nz][ny][nx] = -1
        riped.append((nz, ny, nx, t+1))
        
  ans = riped[-1][3]

  chk = 0
  for i in range(h):
    for j in range(n):
      chk -= sum(store[i][j])
      
  if chk == h * m * n:
    print(ans)
  else:
    print(-1)
else:
  print(-1)