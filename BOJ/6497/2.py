import sys
input = sys.stdin.readline

m, n = map(int, input().split())
while m != 0 and n != 0:
  parent = [i for i in range(m)]

  def findParent(x):
    if x != parent[x]:
      parent[x] = findParent(parent[x])
    return parent[x]

  def union(a, b):
    pa = findParent(a)
    pb = findParent(b)
    
    parent[pb]=pa

  edges = []

  for _ in range(n):
    a, b, c = map(int, input().split())
    
    edges.append((c, a, b))
    
  edges.sort()

  ans = 0

  for e in edges:
    cost, a, b = e
    
    if findParent(a) != findParent(b):
      ans += cost
      union(a, b)
      
  print(ans)
  
  m, n = map(int, input().split())