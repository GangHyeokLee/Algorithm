v, e = map(int, input().split())
edges = []
for _ in range(e):
  a, b, cost = map(int, input().split())
  
  edges.append((cost, a, b))

edges.sort()

parent = [i for i in range(v+1)]

def find(x, parent):
  if x != parent[x]:
    parent[x] = find(parent[x], parent)
    
  return parent[x]

def union(a, b, parent):
  pa = find(a, parent)
  pb = find(b, parent)
  
  
  if pa != pb:
    parent[pa] = pb
    return True
  else:
    return False
  
ans = 0
for eg in edges:
  c, a, b = eg
  if union(a, b, parent):
    ans += c

print(ans)
  
