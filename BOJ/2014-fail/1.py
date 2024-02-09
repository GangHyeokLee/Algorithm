import sys
input = sys.stdin.readline
from heapq import heappop, heappush

k, n = map(int, input().split())

prime = list(map(int, input().split()))

visited = set()
heap = []
max_value = max(prime)

for i in prime:
  heappush(heap, i)

for i in range(n-1):
  element = heappop(heap)
  for x in prime:
    now = element * x
    if len(heap) >= n and max_value < now:
      continue
    if now not in visited:
      heappush(heap, now)
      max_value = max(max_value, now)
      visited.add(now)

print(heappop(heap))