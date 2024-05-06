import sys
from heapq import heappush, heappop

input = sys.stdin.readline

minheap = [] # 중간값 보다 큰 수 저장용
maxheap = [] # 중간값 이하의 수 저장용

for _ in range(int(input())):
  n = int(input())
  
  if len(maxheap) == 0 or len(maxheap) <= len(minheap):
    heappush(maxheap, -n)
  elif len(minheap) == 0 or len(maxheap) > len(minheap):
    heappush(minheap, n)
  if minheap and maxheap and (minheap[0] < -maxheap[0]):
    a = heappop(minheap)
    b = -heappop(maxheap)
    heappush(maxheap, -a)
    heappush(minheap, b)
  
  print(-maxheap[0])