n = int(input())

umul = [int(input()) for _ in range(n)]

edges = []

for i in range(n):
  row = list(map(int, input().split()))
  
  for j in range(n):
    if i == j:
      continue
    edges.append((row[j], i, j))
    
edges.sort()

parent = [i for i in range(n)]


def findParent(x):
  if parent[x] != x:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  if umul[pa] < umul[pb]:
    parent[pb] = pa
  else:
    parent[pa] = pb

visited = [True] * n

# 다 파놓은 상태에서 연결하면서 우물 덮기
ans = sum(umul)
print(ans)

for e in edges:
  cost, a, b = e
  if findParent(a) != findParent(b):
    if visited[a] and visited[b]:
      if umul[a] + umul[b] > cost:
        union(a, b)
        ans -= max(umul[a], umul[b])
        umul[a] = umul[b] = min(umul[a], umul[b])
        ans += cost
      visited[a] = visited[b] = False
    # a 미방문, b 방문
    elif visited[a] and not visited[b]:
      # 새로 파는게 더 비쌈
      if cost < umul[a]:
        ans -= max(umul[a], umul[b])
        ans += cost
        union(a, b)
        umul[a] = umul[b] = min(umul[a], umul[b])
        
      visited[a] = False
    elif not visited[a] and visited[b]:
      if cost < umul[b]:
        ans -= max(umul[a], umul[b])
        ans += cost
        union(a, b)
        umul[a] = umul[b] = min(umul[a], umul[b])
        
      visited[b] = False
      

print(ans)
