nums = []

n = int(input())

for _ in range(n):
  nums.append(int(input()))

for i in range(n):
  for j in range(i+1, n): 
    if nums[i] > nums[j]:
      nums[i], nums[j] = nums[j], nums[i]

for i in nums:
  print(i)