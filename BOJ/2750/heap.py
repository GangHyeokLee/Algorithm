import heapq

nums = []

for _ in range(int(input())):
  heapq.heappush(nums, int(input()))

while len(nums):
  print(heapq.heappop(nums))