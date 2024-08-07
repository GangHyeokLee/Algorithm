from collections import defaultdict
import sys

input = sys.stdin.readline

for _ in range(int(input())):
  v, e = map(int, input().split())
  graph = defaultdict(list)
  
  for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
  visited = [-1 for _ in range(v+1)]

  chk = True
  for i in range(1, v+1):
    if visited[i] == -1 and chk:
      visited[i] = 0
      que = [(i, 0)]
      idx = 0

      while idx < len(que) and chk:
        now, color = que[idx]
        idx += 1
        
        for next in graph[now]:
          if visited[next] == -1:
            que.append((next, abs(color-1)))
            visited[next] = abs(color-1)
          elif visited[next] == visited[now]:
            chk = False
            break
  
  print("YES" if chk else "NO")
  