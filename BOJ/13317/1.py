n, m = 50, 49

print(n, m)

start = 1

edges = []

for i in range(m):
    a, b, c = start, start + 1, -1
    edges.append((a, b, c))
    start += 1

for e in reversed(edges):
    print(" ".join(map(str, e)))
