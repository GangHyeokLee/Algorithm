def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    maps = [[0] * 200 for _ in range(200)]
    
    for r in rectangle:
      x1, y1, x2, y2 = r
      for y in range(2 * y1, (2 * y2)+1):
        for x in range(2 * x1, (2 * x2)+1):
          if maps[y][x] != 2 and (y == 2 * y1 or y == 2 * y2):
            maps[y][x] = 1
          elif maps[y][x] != 2 and (x == 2 * x1 or x == 2 * x2):
            maps[y][x] = 1
          else:
            maps[y][x] = 2
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    queue = [(characterY * 2, characterX * 2, 0)]
    idx = 0
    maps[characterY * 2][characterX * 2] = 0
    
    while idx < len(queue):
      y, x, t = queue[idx]
      idx += 1
      
      if y == 2 * itemY and x == 2 * itemX:
        answer = t // 2
        break
      
      for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        
        if 0 <= ny < len(maps) and 0 <= nx < len(maps) and maps[ny][nx] == 1:
          maps[ny][nx] = 0
          queue.append((ny, nx, t+1))
    
    return answer
  
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))