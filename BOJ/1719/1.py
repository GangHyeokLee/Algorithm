n, m = map(int, input().split())

tp = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
parent = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    tp[i][i] = 0
    parent[i][i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    tp[a][b] = min(tp[a][b], c)
    tp[b][a] = min(tp[b][a], c)
    parent[a][b] = b
    parent[b][a] = a

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tp[i][j] > tp[i][k] + tp[k][j]:
                tp[i][j] = tp[i][k] + tp[k][j]
                parent[i][j] = parent[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            print("-", end=" ")
        else:
            print(parent[i][j], end=" ")
    print()
