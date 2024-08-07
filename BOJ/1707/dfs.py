from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, color, graph, visited):
  visited[start] = color
  for next in graph[start]:
    if visited[next] == -1:
      if not dfs(next, 1 - color, graph, visited):
        return False
    elif visited[next] == color:
      return False
  return True

for _ in range(int(input())):
  v, e = map(int, input().split())
  graph = defaultdict(list)
  
  for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
  visited = [-1 for _ in range(v+1)]
  
  answer = True
  
  for i in range(1, v+1):
    if visited[i] == -1:
      if not dfs(i, 0, graph, visited):
        answer = False
  
  print("YES" if answer else "NO")