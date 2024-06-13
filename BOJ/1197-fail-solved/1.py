from heapq import heappop, heappush

v, e = map(int, input().split())

node = [[] for _ in range(v+1)]

edges = []
for _ in range(e):
  a, b, c = map(int, input().split())
  heappush(edges, (c, a, b))
  
parent = [i for i in range(v+1)]

def findParent(x):
  if parent[x] == x:
    return x
  else:
    parent[x] = findParent(parent[x])
    return parent[x]
  

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  if a<b:
    parent[pb] = pa
  else:
    parent[pa] = pb

cost = 0
while edges:
  weight, a, b = heappop(edges)
  
  if findParent(a) != findParent(b):
    cost += weight
    union(a, b)
print(cost)