n, m = map(int, input().split())

castle = [list(input()) for _ in range(n)]

rotate = [['.'] * n for _ in range(m)]

for i in range(n):
  for j in range(m):
    rotate[j][n - i - 1] = castle[i][j]

row = 0
for c in castle:
  tmp = set(c)
  if len(tmp) == 1 and tmp.pop() == '.':
    row += 1

col = 0
for r in rotate:
  tmp = set(r)
  if len(tmp) == 1 and tmp.pop() == '.':
    col+=1
    
print( max(row, col))