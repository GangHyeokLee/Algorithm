import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

se = []

for i in range(1, n):
  nums[i] = nums[i] + nums[i-1]
  
for _ in range(m):
  i, j = map(int, input().split())
  
  if i == 1:
    print(nums[j-1])
  else:
    print(nums[j-1] - nums[i-2])