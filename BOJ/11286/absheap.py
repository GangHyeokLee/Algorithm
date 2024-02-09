from heapq import heappop, heappush
import sys

input = sys.stdin.readline

heap = []

for _ in range(int(input())):
  x = int(input())

  if x:
    heappush(heap,(abs(x), x))
  elif len(heap) == 0:
    print(0)
  else:
    absolute, original = heappop(heap)
    print(original)