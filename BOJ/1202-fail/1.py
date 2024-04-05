import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, k = map(int, input().split()) #보석, 가방
gems = []
for _ in range(n):
  heappush(gems, list(map(int, input().split())))
bags = sorted([int(input()) for _ in range(k)])

ans = 0
heap = []
# 무게 작은 보석 중 가장 가치 높은 것 넣고
for b in bags:
  while gems and gems[0][0] <= b:
    heappush(heap, -heappop(gems)[1])
  if heap:
    ans -= heappop(heap)
print(ans)