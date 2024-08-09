import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())

loc = []

for _ in range(n):
  a, b = map(int,input().split())
  
  loc.append((min(a, b), max(a, b)))

loc.sort(key=lambda x: (x[1], x[0]))

d = int(input())

heap = []
count = 0

for l in loc:
  h, o = l
  heappush(heap, h)
  start = o - d
  end = o
  
  while heap and heap[0] < start:
    heappop(heap)
  count = max(count, len(heap))
  
print(count)