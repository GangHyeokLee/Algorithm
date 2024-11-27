from heapq import heappush, heappop
from collections import defaultdict

n, m = map(int, input().split())

edges = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())

    edges[a].append((c, b))
    edges[b].append((c, a))

que = [(0, 1)]

dist = [50000 * 50000] * (n + 1)
dist[1] = 0

while que:
    cost, now = heappop(que)

    if dist[now] >= cost:
        for nc, next in edges[now]:
            if cost + nc < dist[next]:
                dist[next] = cost + nc
                heappush(que, (dist[next], next))

print(dist[-1])
