from collections import deque
n = int(input())
balls = deque(enumerate(list(map(int, input().split()))))

while balls:
  i, next = balls.popleft()
  print(i+1, end=" ")
  if not balls:
    break
  for t in range(abs(next if next < 0 else next-1)):
    if next > 0:
      balls.append(balls.popleft())
    else:
      balls.appendleft(balls.pop())