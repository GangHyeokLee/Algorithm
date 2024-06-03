def find(x, parent):
  if x != parent[x]:
    parent[x] = find(parent[x], parent)
  return parent[x]

def union(a, b, parent):
  pa = find(a, parent)
  pb = find(b, parent)
  
  parent[pb] = pa

def solution(n, computers):
    answer = 0
    
    edges = []
    
    for i in range(n):
      for j in range(i+1, n):
        if computers[i][j] == 1:
          edges.append((i, j))
    
    parent = [i for i in range(n)]
    for e in edges:
      i, j = e
      if find(i, parent) != find(j, parent):
        union(i, j, parent)
        
    for i in range(n):
      parent[i] = find(i, parent)
      
    answer = set(parent)
    
    return len(answer)