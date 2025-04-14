from heapq import *
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

forest = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, cost = map(int, input().split())

    forest[a].append((b, cost * 2))
    forest[b].append((a, cost * 2))

que = []
heappush(que, (0, 1))
dist = [float("inf")] * (n + 1)
dist[1] = 0

while que:
    cost, now = heappop(que)

    if dist[now] < cost:
        continue

    for next, d in forest[now]:
        if dist[next] > cost + d:
            dist[next] = cost + d
            heappush(que, (dist[next], next))

wolf = [[float("inf")] * (n + 1) for _ in range(2)]
wolf[0][1] = 0
heap = [(0, 1, 0)]

while heap:
    cost, now, state = heappop(heap)
    if wolf[state][now] < cost:
        continue
    for next, d in forest[now]:
        if state == 0:
            new_time = cost + d // 2
        else:
            new_time = cost + d * 2

        if wolf[abs(state - 1)][next] > new_time:
            wolf[abs(state - 1)][next] = new_time
            heappush(heap, (new_time, next, abs(state - 1)))

result = 0
for i in range(2, n + 1):
    if dist[i] < min(wolf[0][i], wolf[1][i]):
        result += 1
print(result)
