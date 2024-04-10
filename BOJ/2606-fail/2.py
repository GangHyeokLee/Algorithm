n = int(input()) # nodes
e = int(input()) # edges

# union find용 부모 
parent = [i for i in range(n+1)]

def findParent(x):
  # 자기랑 연결된 root 찾기
  # root는 자기 자신을 가리킴
  px = x
  while px != parent[px]:
    px = parent[px]
    
  # parent 리스트에도 root로 업데이트
  parent[x] = px
  return px

def union(x, y):
  px = findParent(x)
  py = findParent(y)
  
  # 그냥 왼쪽 그룹에 오른쪽 그룹이 하위로 들어가기
  parent[py] = px
  
for _ in range(e):
  a, b = map(int, input().split())
  union(a, b)

# Parent 관계 전수조사해서 정리하기
for i in range(1, n+1):
  parent[i] = findParent(i)

# 1번 컴퓨터의 root 찾기
infestedP = parent[1]

ans = 0
for i in parent:
  if i == infestedP:
    ans += 1
# 1번 컴퓨터 제외
print(ans - 1)