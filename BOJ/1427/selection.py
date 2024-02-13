n = input()

nums = []

for i in n:
  nums.append(int(i))

sorted_nums = []

for i in range(len(nums)):
  for j in range(i+1, len(nums)): 
    if nums[i] < nums[j]:
      nums[i], nums[j] = nums[j], nums[i]

for i in nums:
  sorted_nums.append(str(i))

print(''.join(sorted_nums))