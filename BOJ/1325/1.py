import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

adj = defaultdict(list)

for _ in range(m):
  # a가 b를 신뢰
  # b해킹당하면 a해킹 가능 역은 안 될 듯
  a, b = map(int, input().split())
  
  adj[b].append(a)

ans = []
maxHacked = 0
# 컴퓨터 전체 돌면서 bfs로 탐색 시작
for i in range(1, n+1):
  visited = [True] * (n+1)
  visited[i] = False
  
  hacked = []
  hacked.append(i)
  idx = 0
  while idx < len(hacked):
    now = hacked[idx]
    idx += 1
    for next in adj[now]:
      if visited[next]:
        visited[next] = False
        hacked.append(next)
  
  maxHacked = max(maxHacked, len(hacked))
  ans.append((len(hacked), i))

for a in ans:
  if a[0] == maxHacked:
    print(a[1], end=" ")