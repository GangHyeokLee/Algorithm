from collections import defaultdict

def maximalRectangle(self, matrix: list[list[str]]) -> int:
  r = len(matrix)
  c = len(matrix[0])
  
  dy = [0, 0, 1, -1]
  dx = [1, -1, 0, 0]
  
  ans = 400000000
  
  for i in range(r):
    for j in range(c):
      if matrix[i][j] == "1":
        matrix[i][j] = "0"
        que = [(i, j)]
        
        xs = defaultdict(list)
        ys = defaultdict(list)
        
        idx = 0
        
        xs[j].append(i)
        ys[i].append(j)
        
        while idx < len(que):
          y, x = que[idx]
          idx += 1
          
          for d in range(r):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < r and 0 <= nx < c and matrix[ny][nx] == "1":
              matrix[ny][nx] = "0"
              que.append((ny, nx))
              xs[nx].append(ny)
              ys[ny].append(nx)
        minX = 4000
        minY = 4000
        for x in xs.values():
          minX = min(max(x) - min(x) + 1, minX)
        
        for y in ys.values():
          minY = min(max(y) - min(y) + 1, minY)
        ans = min(ans, minY * minX)
  return ans
        
  
print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))