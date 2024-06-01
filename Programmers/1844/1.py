def solution(maps):
    answer = 0
    
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    
    queue = [(0, 0, 1)]
    idx = 0
    
    maps[0][0] = 0
    found = -1
    while idx < len(queue):
      y, x, t = queue[idx]
      idx += 1
      
      if y == len(maps)-1 and x == len(maps[0])-1:
        found = t
        break
      
      for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        
        if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx]:
          maps[ny][nx] = 0
          queue.append((ny, nx, t+1))
    
    return found