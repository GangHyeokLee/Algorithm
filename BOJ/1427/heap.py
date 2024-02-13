import heapq

n = input()

nums = []

for i in n:
  heapq.heappush(nums, -int(i))

sorted_nums = []

while len(nums):
  sorted_nums.append(str(-heapq.heappop(nums)))

print(''.join(sorted_nums))