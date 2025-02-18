n = int(input())
m = int(input())

buses = [list(map(int, input().split())) for _ in range(m)]

dist = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dist[i][i] = 0

for a, b, c in buses:
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(n + 1):
    for j in range(n + 1):
        if dist[i][j] == float("inf"):
            dist[i][j] = 0

for i in range(1, n + 1):
    print(" ".join(map(str, dist[i][1:])))
