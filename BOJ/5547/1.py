# y좌표가 짝수면 x-1, x
# y좌표가 홀수면 x, x+1


w, h = map(int, input().split())

house = [[0] * (w+2)]
house += [[0] + list(map(int, input().split())) + [0] for _ in range(h)]
house.append([0] * (w+2))

w += 2
h += 2

dy = [0, 0, 1, 1, -1, -1]

# 홀수용 dx 좌우 하 상
dxo = [1, -1, 1, 0, 1, 0]
# 짝수용
dxe = [1, -1, -1, 0, -1, 0]

que = [(0, 0)]
idx = 0
house[0][0] = 5

while idx < len(que):
  y, x = que[idx]
  idx += 1
  
  for d in range(6):
    ny = y + dy[d]
    nx = x + (dxo[d] if y%2 else dxe[d])
    
    if 0 <= ny < h and 0 <= nx < w and house[ny][nx] == 0:
      house[ny][nx] = 5
      que.append((ny, nx))
      
ans = 0
for i in range(h):
  for j in range(w):
    
    if house[i][j] == 1:
      wall = 0
      que = [(i, j)]
      idx = 0
      house[i][j] = 0
      while idx < len(que):
        y, x = que[idx]
        idx += 1
        wall += 6
        
        for d in range(6):
          ny = y + dy[d]
          nx = x + (dxo[d] if y%2 else dxe[d])
          
          # 다음 건물이랑 붙어 있으면 que에 추가하고 wall 값 하나 빼기
          if 0 <= ny < h and 0 <= nx < w and house[ny][nx] == 1:
            house[ny][nx] = 0
            que.append((ny, nx))
            wall -= 1
          # 이미 지나온 건물이라 0 혹은 건물로 둘러 쌓여진 부분이라 0이라서 wall 하나 빼기
          elif 0 <= ny < h and 0 <= nx < w and house[ny][nx] == 0:
            wall -= 1
      ans += wall
      

print(ans)