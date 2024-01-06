import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = []

for _ in range(n):
  maze.append(list(map(int, list(input().rstrip()))))

r = [1, 0, -1, 0]
c = [0, 1, 0, -1]

dq = deque()
chk = True

dq.append((0, 0, 1))
while dq and chk:
  i, j, count = dq.popleft()
  
  for d in range(4):
    dr = i + r[d]
    dc = j + c[d]

    if 0 <= dr < n and 0 <= dc < m and maze[dr][dc] == 1:
      if [dr, dc] == [n-1, m-1]:
        print(count+1)
        chk = False
        break

      dq.append((dr, dc, count+1))

