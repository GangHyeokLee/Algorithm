from collections import deque

n = int(input())
apples = [list(map(int, input().split())) for _ in range(int(input()))]
order = deque(list(input().split()) for _ in range(int(input())))

snake = deque()
snake.append([1, 1])

LD = { 'L': -1, 'D': 1}
directions = [ [-1, 0], [0, 1], [1, 0], [0, -1]] # 오른쪽으로 갈 때 D나오면 1더하면 아래, 그런 식
ans = 0
dir = 1

while True:  
  ans += 1
  
  # 새로운 칸
  ny, nx = snake[-1][0] + directions[dir][0], snake[-1][1] + directions[dir][1]
  if not (1 <= ny <= n and 1 <= nx <= n and [ny, nx] not in snake):# 벽이나 몸이랑 부딪히는 지 확인
    break
  
  snake.append([ny, nx])
  if [ny, nx] not in apples: #사과가 아니면    
    snake.popleft()
  else:
    apples.remove([ny, nx]) #사과 먹어서 없어짐
      
  if order and ans == int(order[0][0]): # 명령 시간 됐을 때
    dir = (dir + LD[order[0][1]]) % 4
    order.popleft()
  
print(ans)