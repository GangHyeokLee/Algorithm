n, k = map(int, input().split())
p = list(list(map(int, input().split())) for _ in range(n))

for t in range(n):
  for i in range(n):
    for j in range(n):
      p[i][j] = min(p[i][j], p[i][t] + p[t][j])

visited = [False] * n
result = 10 * 1000 * 1000
  
def recursive(pos, cnt, cost):
    global result

    if cnt == n:
        result = min(result, cost)
        return

    for next in range(n):
        if not visited[next]:
            visited[next] = True
            recursive(next, cnt + 1, cost + p[pos][next])
            visited[next] = False

visited[k] = True
recursive(k, 1, 0)
print(result)

