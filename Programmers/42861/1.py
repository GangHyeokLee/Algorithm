def find(x, parent):
  if x != parent[x]:
    parent[x] = find(parent[x], parent)
  return parent[x]

def union(a, b, parent):
  pa = find(a, parent)
  pb = find(b, parent)
  
  parent[pa] = pb

def solution(n, costs):
  answer = 0
    
  costs.sort(key = lambda x: x[2])
  
  parent = [i for i in range(n+1)]
  
  for e in costs:
    a, b, cost = e
    if find(a, parent) != find(b, parent):
      answer += cost
      union(a,b, parent)
  
  return answer