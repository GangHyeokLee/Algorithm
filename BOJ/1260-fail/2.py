import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, v = map(int, input().split())

adjg = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  adjg[a].append(b)
  adjg[b].append(a)
  
for i in adjg:
  i.sort()

visited = [True] * (n+1)
visited[v] = False
def dfs(start):
  print(start, end=" ")
  for i in adjg[start]:
    if visited[i]:
      visited[i] = False
      dfs(i)
      # 이미 들른 곳 안 가기 위해 visited는 그대로 냅둠
dfs(v)
print()
# deque 안 쓰고 큐 구현
idx = 0
que = []

visited = [True] * (n+1)
visited[v] = False
que.append(v)
while idx < len(que):
  now = que[idx]
  print(now, end=" ")
  idx += 1
  
  for i in adjg[now]:
    # now와 연결됐고 방문 안 했을 경우
    if visited[i]:
      que.append(i)
      visited[i] = False