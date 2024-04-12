import math

n, m = map(int, input().split())

def calCost(a, b):
  dx = coord[a-1][0] - coord[b-1][0]
  dy = coord[a-1][1] - coord[b-1][1]
  
  return math.sqrt(dx ** 2 + dy ** 2)

def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  parent[pb] = pa

coord = []

for i in range(n):
  x, y = map(int, input().split())
  
  coord.append((x, y))

eg = []

for _ in range(m):
  a, b = map(int, input().split())
  cost = calCost(a, b)
  eg.append((cost, a, b))

eg.sort()
parent = [i for i in range(n+1)]

for e in eg:
  cost, a, b = e
  # 부모 다르면
  if findParent(a) != findParent(b):
    union(a, b)

eg.clear()

# 2중 포문으로 거리 계산
for i in range(1, n):
  for j in range(i+1, n+1):
    eg.append((calCost(i, j), i, j))
eg.sort()
ans = 0

for e in eg:
  cost, a, b = e
  if findParent(a) != findParent(b):
    ans += cost
    union(a, b)
    
print(f"{ans:.2f}")