def findParent(x, parent):
  if x != parent[x]:
    parent[x] = findParent(parent[x], parent)
  return parent[x]

def union(a, b, parent):
  
  pa = findParent(a, parent)
  pb = findParent(b, parent)
  
  parent[pb] = pa

def solution(n, wires):
    answer = 10000
    
    for skip in range(n):
      parent = [i for i in range(n+1)]
      for idx, w in enumerate(wires):
        if idx != skip:
          a, b = w
          if findParent(a, parent) != findParent(b, parent):
            union(a, b, parent)
          
      for i in range(1, n+1):
        parent[i] = findParent(parent[i], parent)
      
      parent.sort()
      for i in range(1, n):
        if parent[i] != parent[i+1]:
          answer = min(answer, abs(i - (n-i)))
    
    return answer
  
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))