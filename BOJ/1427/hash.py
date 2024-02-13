n = input()

nums = [0] * 10

for i in n:
  nums[int(i)] += 1 

ans = []

for i in range(9, -1, -1):
  for j in range(nums[i]):
    ans.append(str(i))

print(''.join(ans))
