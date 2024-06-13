def find(x, parent):
  if x != parent[x]:
    parent[x] = find(parent[x], parent)
  return parent[x]

def union(a, b, parent):
  pa = find(a, parent)
  pb = find(b, parent)
  
  parent[pb] = pa

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        for e in edges:
          a, b = e
          if find(a, parent) != find(b, parent):
            union(a, b, parent)
            
        for i in range(n):
          parent[i] = find(parent[i], parent)
          
        
        return parent[source] == parent[destination]