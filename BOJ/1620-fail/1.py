import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poke = {}
idx = {}

for i in range(n):
  mon = input().rstrip()
  idx[i+1] = mon
  poke[mon.lower()] = i+1
  
for i in range(m):
  q = input().rstrip()
  
  if q.lower() in poke:
    print(poke[q.lower()])
  else:
    print(idx[int(q)])