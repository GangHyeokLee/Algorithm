from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

road = defaultdict(list)

for _ in range(m):
  a, b = map(int, input().split())
  
  road[a].append(b)
  road[b].append(a)

que = [(1, 0)]
idx = 0
visited = [-1 for _ in range(n+1)]

chk = True
for i in range(1, n+1):
  if visited[i] == -1 and chk:
    visited[i] = 0
    que = [(i, 0)]
    idx = 0

    while idx < len(que) and chk:
      now, color = que[idx]
      idx += 1
      
      for next in road[now]:
        if visited[next] == -1:
          que.append((next, abs(color-1)))
          visited[next] = abs(color-1)
        elif visited[next] == visited[now]:
          chk = False
          break

if chk:
  one = 0
  for i in range(1, n+1):
    if visited[i]:
      one += 1
  print(one * (n-one) * 2)
else:
  print(0)