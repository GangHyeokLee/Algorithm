from collections import deque

n = int(input())
b = list(map(int, input().split()))

balloons = deque()

ans = []
for i, j in enumerate(b):
  balloons.append((i+1, j))


while len(balloons) > 1:
  index, next = balloons.popleft()
  ans.append(index)

  if next > 0:
    for _ in range(next-1):
      balloons.append(balloons.popleft())
  else:
    for _ in range(abs(next)):
      balloons.appendleft(balloons.pop())

ans.append(balloons[0][0])

print(' '.join(map(str,ans)))