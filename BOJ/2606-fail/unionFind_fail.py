import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
m = int(input())

parent = [-1] * (n+1)

def find_root(n):
  if parent[n] == n:
    return n
  parent[n] = find_root(parent[n])
  return parent[n]

for _ in range(m):
  if n == 1:
    break
  a, b = map(int, input().split())
  
  if parent[a] == -1 and parent[b] == -1:
    parent[a] = a
    parent[b] = a
  elif parent[b] != -1:
    parent[a] = b
  else:
    parent[b] = a
  
for i in range(1, len(parent)):
  parent[i] = find_root(parent[i])

ans = 0

for i in range(2, len(parent)):
  if parent[i] == parent[1]:
    ans += 1
print(ans)