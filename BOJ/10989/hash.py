import heapq
import sys

input = sys.stdin.readline

nums = [0] * 10001

for _ in range(int(input())):
  nums[int(input())]+=1

for i in range(len(nums)):
  if nums[i] > 0:
    for j in range(nums[i]):
      print(i)