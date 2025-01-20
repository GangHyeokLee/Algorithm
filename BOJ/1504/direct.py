from heapq import *

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for a, b, c in [map(int, input().split()) for _ in range(m)]:
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

quem = []
quem.append((0, 1))

dist = [200000 * 800 * 2 for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
dist[1] = 0
while quem:
    cost, now = heappop(quem)

    if dist[now] < cost:
        continue

    for next, d in edges[now]:
        if dist[next] > cost + d:
            dist[next] = cost + d
            parent[next] = now
            heappush(quem, (dist[next], next))

now = n

chk1 = False
chk2 = False

while next != now:
    now = next
    next = parent[now]

    if next == v1:
        chk1 = True

    if next == v2:
        chk2 = True

print(chk1, chk2)
