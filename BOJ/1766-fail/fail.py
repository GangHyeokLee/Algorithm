import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)
tree = [[] for i in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  
  parent[b] = a
  tree[a].append(b)
  

iv = []

for i in range(n+1):
  tree[i].sort()


for i, v in enumerate(parent):
  if i == 0:
    continue
  if v == 0:
    iv.append(i)
  
iv.sort()
for i in iv:
  print(i, end=" ")
  for j in sorted(tree[i]):
    print(j, end=" ")