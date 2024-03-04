from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())

queue = []
for _ in range(n):
  x = int(input())
  
  if x:
    heappush(queue, x)
  elif len(queue):
    print(heappop(queue))
  else:
    print(0)