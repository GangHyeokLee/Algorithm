import sys
input = sys.stdin.readline

def find(x):
  if x == parent[x]:
    return x
  else:
    p = find(parent[x])
    parent[x] = p
    return parent[x]
  
def union(x, y):
  x = find(x)
  y = find(y)

  if x!= y:
    parent[y] = x
    number[x] += number[y]

tc = int(input())

for _ in range(tc):
  parent = dict()
  number = dict()

  for _ in range(int(input())):
    x, y = input().split()

    if x not in parent:
      parent[x] = x
      number[x] = 1
    if y not in parent:
      parent[y] = y
      number[y] = 1

    union(x, y)
    print(number[find(x)])