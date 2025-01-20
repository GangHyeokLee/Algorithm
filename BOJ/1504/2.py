import sys
from heapq import *

input = sys.stdin.readline
limit = 200000 * 800 * 1000 * 2


def dij(start, end, n, edges):
    que = []
    dist = [limit for _ in range(n + 1)]

    que.append((0, start))
    dist[start] = 0

    idx = 0
    visited = [False] * (n + 1)

    while idx < len(que):
        cost, now = que[idx]
        idx += 1

        for next, d in edges[now]:
            if not visited[next]:
                que.append((cost + d, next))
                visited[now] = True

                dist[next] = min(dist[next], cost + d)

    return dist[end]


n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for a, b, c in [map(int, input().split()) for _ in range(m)]:
    edges[a].append((b, c))
    edges[b].append((a, c))

v1, v2 = map(int, input().split())

v12 = dij(v1, v2, n, edges)

s1 = dij(1, v1, n, edges)
s2 = dij(1, v2, n, edges)

e1 = dij(v1, n, n, edges)
e2 = dij(v2, n, n, edges)

ans = min(s1 + v12 + e2, s2 + v12 + e1)

print(ans if ans < limit else -1)
