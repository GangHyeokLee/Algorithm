from heapq import heappush, heappop

n = int(input())
heap = []
for _ in range(n):
  nums = list(map(int, input().split()))
  for i in nums:
    heappush(heap, i)
  while len(heap) > n:
    heappop(heap)
  
print(heappop(heap))