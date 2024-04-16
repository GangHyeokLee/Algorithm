# 유니온 파인드 ㄱ
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  parent[pb] = pa
  
for _ in range(m):
  a, b = map(int, input().split())
  
  if findParent(a) != findParent(b):
    union(a, b)
    

for i in range(1, n+1):
  findParent(i)

print(len(set(parent[1:])))