import heapq
import sys

input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
  heapq.heappush(nums, int(input()))

while nums:
  print(heapq.heappop(nums))