dice = [0] * 7

nums = list(map(int, input().split()))

for i in nums:
  dice[i] += 1
  
nums = list(set(nums))

if len(nums) == 1:
  print(10000 + nums[0] * 1000)
elif len(nums) == 2:
  for i in range(1, 7):
    if dice[i] == 2:
      print(1000 + i * 100)
else:
  print(max(nums) * 100)