import sys
input = sys.stdin.readline

n = int(input())

tree = {}

parent = [-1] * (n+1)

for _ in range(n):
  p, l, r = map(int, input().split())

  tree[p] = []
  tree[p].append(l)
  tree[p].append(r)

  if parent[p] == -1:
    parent[p] = p

  if l != -1:
    parent[l] = p
  if r != -1:
    parent[r] = p

def findParent(p):
  if parent[p] == p:
    return p
  parent[p] = findParent(parent[p])
  return parent[p]

for i in range(1, len(parent)):
  parent[i] = findParent(parent[i])

root = parent[-1]

order = []
def inorder(parent, level):
  [l, r] = tree[parent]

  if l != -1:
    inorder(l, level+1)

  order.append([parent, level, len(order)+1])

  if r != -1:
    inorder(r, level+1)

inorder(root, 1)
levels = [[] for i in range(10000)]

for i in order:
  levels[i[1]].append(i[2])

width = [0]
for i in levels:
  if len(i):
    width.append(max(i) - min(i) + 1)

ans = [-1, -1]
for i, v in enumerate(width):
  if ans[1] < v:
    ans = [i, v]

print(ans[0], ans[1])