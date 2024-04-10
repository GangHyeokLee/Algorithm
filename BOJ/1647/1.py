import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 크루스칼로 최소 신장 트리 만들고
# 엣지 중에 가장 큰 것 빼고 구하면 될 듯

parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
  a, b, c = map(int, input().split())
  
  edges.append((c, a, b))

edges.sort()

def findParent(x):
  if x == parent[x]:
    return x
  else:
    parent[x] = findParent(parent[x])
    return parent[x]
  
def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  # 굳이 a, b비교할 필요 없을 듯
  parent[pb] = pa

ans = []
for e in edges:
  cost, a, b = e
  
  if findParent(a) != findParent(b):
    ans.append(cost)
    union(a, b)

# ans에서 최댓값 빼기
ans.sort()
ans.pop()
print(sum(ans))