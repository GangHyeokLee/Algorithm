import heapq
import sys

input = sys.stdin.readline

code = []

for _ in range(int(input())):
  heapq.heappush(code, list(input().split()))

while len(code):
  a = heapq.heappop(code)

  print(a[0], a[1])