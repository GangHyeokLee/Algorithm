n = int(input())

nums = []
for i in range(n):
  tmp = str(i)
  chars = []
  for c in tmp:
    chars.append(int(c))
  if i + sum(chars) == n:
    nums.append(i)
  
print(min(nums) if len(nums) else 0)