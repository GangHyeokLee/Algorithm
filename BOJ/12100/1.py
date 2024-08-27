import copy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def move(dir, board):
  if dir == 0: # 좌
    for i in range(n):
      tmp = []
      for j in range(n):
        if tmp and board[i][j] and tmp[-1] == board[i][j]:
          tmp[-1] *= -2
        elif board[i][j]:
          tmp.append(board[i][j])
      for j in range(n):
        board[i][j] = abs(tmp[j]) if j < len(tmp) else 0
        
  elif dir == 1: # 우
    for i in range(n):
      tmp = []
      for j in range(n-1, -1, -1):
        if tmp and board[i][j] and tmp[-1] == board[i][j]:
          tmp[-1] *= -2
        elif board[i][j]:
          tmp.append(board[i][j])
      for j in range(n):
          board[i][n-j-1] = abs(tmp[j]) if j < len(tmp) else 0
          
  elif dir == 2: #좌
    for j in range(n):
      tmp = []
      for i in range(n):
        if tmp and board[i][j] and tmp[-1] == board[i][j]:
          tmp[-1] *= -2
        elif board[i][j]:
          tmp.append(board[i][j])
      for i in range(n):
        board[i][j] = abs(tmp[i]) if i < len(tmp) else 0
  
  elif dir == 3: #우
    for j in range(n):
      tmp = []
      for i in range(n-1, -1, -1):
        if tmp and board[i][j] and tmp[-1] == board[i][j]:
          tmp[-1] *= -2
        elif board[i][j]:
          tmp.append(board[i][j])
      for i in range(n):
        board[n-i-1][j] = abs(tmp[i]) if i < len(tmp) else 0
  
  return board

ans = []

def dfs(count, board):
  if count == 5:
    for b in board:
      ans.append(max(b))
    return
  
  for d in range(4):
    dfs(count+1, move(d, copy.deepcopy(board)))
    
dfs(0, board)
print(max(ans))
    