import sys
from heapq import heappush, heappop
input = sys.stdin.readline

for _ in range(int(input())):
  n = int(input())
  heap=[]
  for i in map(int, input().split()):
    heappush(heap, i)
  
  ans = 0
  while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    ans += a+b
    heappush(heap, a+b)
    
  print(ans)