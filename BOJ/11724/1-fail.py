import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nodes = [[] for i in range(n+1)]

if m==0:
  print(n)
else:
  for _ in range(m):
    t = list(map(int, input().split()))

    nodes[t[0]].append(t[1])
    nodes[t[1]].append(t[0])
    
  visited = [False for i in range(n+1)]

  count = 0
  for i in range(n):
    if i==0:
      continue
    if visited[i]:
      continue
    
    count+=1
    visited[i] = True
    queue = list(nodes[i])
    for j in queue:
      if visited[j]:
        continue

      visited[j] = True
      for k in nodes[j]:
        queue.append(k)

  print(count)