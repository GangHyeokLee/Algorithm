import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

noListen = defaultdict()
for _ in range(n):
  noListen[input().strip()] = True

noListenSee = []
for _ in range(m):
  p = input().strip()
  if p in noListen:
    noListenSee.append(p)

noListenSee.sort()
print(len(noListenSee))
for i in noListenSee:
  print(i)