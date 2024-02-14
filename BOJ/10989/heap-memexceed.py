import heapq
import sys

input = sys.stdin.readline

nums = []

for _ in range(int(input())):
  heapq.heappush(nums, int(input()))

while len(nums):
  print(heapq.heappop(nums))