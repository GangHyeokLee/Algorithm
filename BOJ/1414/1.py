# print(ord('a')-96): 1
# print(ord('A')-38): 27

n = int(input())


eg = []
total = 0
for i in range(n):
  row = list(input().strip())
  for r in range(n):
    # 대소문자에 따라 숫자로 변경
    if row[r].isupper():
      row[r] = ord(row[r]) - 38
    elif row[r].islower():
      row[r] = ord(row[r]) - 96
    else:
      row[r] = int(row[r])
    # 랜선 길이 저장
    if row[r]:
      total += row[r]
      eg.append((row[r], i, r))
eg.sort()
def findParent(x):
  if x != parent[x]:
    parent[x] = findParent(parent[x])
  return parent[x]

def union(a, b):
  pa = findParent(a)
  pb = findParent(b)
  
  parent[pb] = pa

ans = 0
parent = [i for i in range(n)]
for e in eg:
  cost, a, b = e
  if findParent(a) != findParent(b):
    ans += cost
    union(a, b)

for i in range(n):
  findParent(i)
    
print(total - ans if len(set(parent)) == 1 else -1)