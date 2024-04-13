n, m = map(int, input().split())

college = list(input().split())
parent = [i for i in range(n+1)]

def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  parent[pb] = pa

roads = []
for _ in range(m):
  a, b, cost = map(int,input().split())
  roads.append((cost, a, b))
roads.sort()

ans = 0
for r in roads:
  cost, a, b = r
  # 성별 다르고 다른 그룹일 때
  if college[a-1] != college[b-1] and findParent(a) != findParent(b):
    ans += cost
    union(a, b)
    
# 모든 학교 연결 잘 됐는지 확인하기
for i in range(n+1):
  findParent(i)

chk = set(parent[1:])

# 연결 잘 됐다
if len(chk) == 1:
  print(ans)
else:
  print(-1)
