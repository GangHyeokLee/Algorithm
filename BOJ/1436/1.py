n = int(input())

nums = [666]

for i in range(1, n):
  tmp = nums[-1]
  while True:
    tmp += 1
    if '666' in str(tmp):
      nums.append(tmp)
      break
  
print(nums[-1])