n = int(input())
e = int(input())

edges = []
for _ in range(e):
  a, b, c = map(int, input().split())
  
  edges.append((c, a, b))

# 비용에 따라 정렬
edges.sort()

# 부모 노드를 저장할 리스트
parent = [i for i in range(n+1)]

def findParent(x):
  if x == parent[x]:
    return x
  else:
    # 부모 노드도 root로 업데이트 해주기
    parent[x] = findParent(parent[x])
    return parent[x]
  
def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  # 루트끼리 합치기
  if a<b:
    parent[pb] = pa
  else:
    parent[pa] = pb
    
ans = 0
for e in edges:
  cost, a, b = e
  if findParent(a) != findParent(b):
    ans += cost
    union(a, b)
    
print(ans)