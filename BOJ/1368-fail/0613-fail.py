n = int(input())
edges = []

for i in range(n):
  edges.append((int(input()), 0, i+1))  

field = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
  for j in range(i+1, n):
    edges.append((field[i][j], i+1, j+1))
    
edges.sort()

def find(x, parent):
  if x != parent[x]:
    parent[x] = find(parent[x], parent)
    
  return parent[x]

def union(a, b, parent):
  pa = find(a, parent)
  pb = find(b, parent)
  if pa < pb:
    parent[pb] = pa
  else:
    parent[pa] = pb
    
parent = [i for i in range(n+1)]
ans = 0
for e in edges:
  cost, a, b = e
  if find(a, parent) != find(b, parent):
    union(a, b, parent)
    ans += cost
print(ans)
    
