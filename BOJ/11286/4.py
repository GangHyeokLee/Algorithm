import sys
from heapq import heappop, heappush

input = sys.stdin.readline

heap = []
for _ in range(int(input())):
  n = int(input())
  if n == 0 and heap:
    print(heappop(heap)[1])
  elif n == 0:
    print(0)
  else:
    heappush(heap, (abs(n), n))
