n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

max_cost = 1000000 * 5000
dist = [max_cost] * (n + 1)
dist[1] = 0

chk = False
for i in range(1, n + 1):
    for s, e, c in edges:
        if dist[s] == max_cost:
            continue
        if dist[s] + c < dist[e]:
            dist[e] = dist[s] + c

for i in range(1, n):
    for a, b, c in edges:
        if dist[a] != max_cost and dist[a] + c < dist[b]:
            dist[b] -= max_cost
            chk = True

if chk:
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i] if dist[i] < max_cost else -1)
