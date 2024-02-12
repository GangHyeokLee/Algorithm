import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())

parent = []

for i in range(n+1):
  parent.append(i)
  


def find(parent, x):
  if parent[x] != x:
    parent[x] = find(parent, parent[x])
  return parent[x]

def union(parent, x, y):
  x = find(parent, x)
  y = find(parent, y)

  if x < y:
    parent[y] = x
  else:
    parent[x] = y


for _ in range(m):
  u, v = map(int, input().split())
  union(parent, u, v)


for i in range(1, n+1):
  parent[i] = find(parent, i)

print(len(set(parent)) - 1)

