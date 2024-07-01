n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

i = 0
j = len(nums) - 1

count = 0
while i < j:
  if nums[i] + nums[j] < x:
    i+=1
  elif nums[i] + nums[j] > x:
    j -= 1
  else:
    i+=1
    j-=1
    count += 1
    
print(count)
    
  