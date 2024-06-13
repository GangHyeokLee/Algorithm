import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split())
gems = []

for _ in range(n):
  heappush(gems, list(map(int, input().split())))
bags = []

for _ in range(k):
  bags.append(int(input()))

bags.sort()

w = 0
ans = 0
heap = []

for b in bags:
  while gems and gems[0][0] <= b:
    heappush(heap, -heappop(gems)[1])
  if heap:
    ans -= heappop(heap)
  
  
    
print(ans)