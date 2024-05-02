import sys

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]

def union(a, b):
  pa = find(a)
  pb = find(b)
  
  if pa == pb:
    return False
  
  parent[pb] = pa
  return True
  
for e in edges:
  a, b = e
  union(a, b)

for i in range(1, n+1):
  find(i)

print(len(set(parent[1:])))