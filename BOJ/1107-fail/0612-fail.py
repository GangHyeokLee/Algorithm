m = int(input())

n = int(input())

buttons = list(map(int, input().split()))

min_count = abs(100 - m)

for nums in range(1000001):
  nums = str(nums)
  
  for j in range(len(nums)):
    if int(nums[j]) in buttons:
      break
    elif j == len(nums) - 1:
      min_count = min(min_count, abs(int(nums) - m) + len(nums))
print(min_count)