n, m = map(int, input().split())

def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  parent[pb] = pa
  

parent = [i for i in range(n+1)]

mineg = []
maxeg = []

for _ in range(m+1):
  a, b, updown = map(int, input().split())
  # 오르막이 1, 내리막이 0으로 수정
  updown = abs(updown-1)
  
  mineg.append((updown, a, b))
  maxeg.append((-updown, a, b))
  
mineg.sort()
maxeg.sort()

min = 0
for e in mineg:
  cost, a, b = e
  if findParent(a) != findParent(b):
    min += cost
    union(a, b)


parent = [i for i in range(n+1)]

max = 0
for e in maxeg:
  cost, a, b = e
  if findParent(a) != findParent(b):
    max += cost
    union(a, b)
    
print(max ** 2 - min**2)