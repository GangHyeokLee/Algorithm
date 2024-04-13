n, m, k = map(int, input().split())
# in의 시간복잡도 때문에 set으로 변경
power = set(map(int, input().split()))

cable = [list(map(int, input().split())) for _ in range(m)]
costCable = []
parent = [i for i in range(n+1)]


def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  # 새로온 노드가 발전소
  if a in power:
    # 이미 발전소 있어요
    if pb in power:
      return False
    # 새로운 발전소 추가
    else:
      parent[pb] = a
  elif b in power:
    # 이미 발전소 있어요
    if pa in power:
      return False
    # 새로운 발전소 추가
    else:
      parent[pa] = b
  # 발전소 있는 도시랑 없는 도시 합치기
  elif pa in power and pb not in power:
    parent[pb] = pa
  elif pa not in power and pb in power:
    parent[pa] = pb
  # 둘 다 발전소 없을 때
  elif pa not in power and pb not in power:
    parent[pb] = pa
  # pa, pb 둘 다 발전소
  else:
    return False
  return True
    
  
  parent[pb] = pa
for c in cable:
  u, v, w = c
  costCable.append((w, u, v))
  
costCable.sort()

ans = 0
for c in costCable:
  cost, u, v = c
  
  if findParent(u) != findParent(v) and union(u, v):
    ans += cost
print(ans)