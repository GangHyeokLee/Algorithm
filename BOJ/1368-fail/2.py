n = int(input())

edges = []

for i in range(n):
  edges.append((int(input()), 0, i+1))
  
for i in range(n):
  row = list(map(int, input().split()))
  
  for j in range(n):
    if i == j:
      continue
    edges.append((row[j], i+1, j+1))
    
edges.sort()

def findParent(x):
  if parent[x] != x:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  if pa == pb:
    return False
  else:
    parent[pa] = pb
    return True

parent = [i for i in range(n+1)]

ans = 0
for e in edges:
  cost, a, b = e
  if union(a, b):
    ans += cost

print(ans)