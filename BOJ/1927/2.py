from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
  op = int(input())
  if op == 0:
    print(heappop(heap) if heap else 0)
  else:
    heappush(heap, op)