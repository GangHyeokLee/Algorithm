# adj는 시간초과뜸 백만개 전부 탐색해야돼서 그런듯 합니다.
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())

adjm = [[0] * (n + 1) for _ in range(n + 1)]

# n 1000개라서 그냥 인접매트릭스씀
for _ in range(m):
  a, b = map(int, input().split())
  adjm[a][b] = 1
  adjm[b][a] = 1

visited = [True] * (n + 1)
visited[v] = False

def dfs(start, ans):
  ans.append(start)
  if len(ans) == n:
    print(" ".join(map(str, ans)))
  for i in range(1, n+1):
    if adjm[start][i] and visited[i]:
      visited[i] = False
      dfs(i, ans)
      visited[i] = True
      if len(ans) == n:
        return
dfs(v, [])

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
  
  for i in range(1, n+1):
    # now와 연결됐고 방문 안 했을 경우
    if adjm[now][i] and visited[i]:
      que.append(i)
      visited[i] = False
