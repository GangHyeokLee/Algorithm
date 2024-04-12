n = int(input())

adj = [list(map(int, input().split())) for _ in range(n)]

eg = []
for i in range(n-1):
  for j in range(i+1, n):
    eg.append((adj[i][j], i, j))
    
def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  parent[pb] = pa
  
parent = [i for i in range(n)]
eg.sort()
ans = 0
for e in eg:
  cost, a, b = e
  if findParent(a) != findParent(b):
    ans += cost
    union(a, b)
print(ans)