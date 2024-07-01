n = int(input())

nums = sorted(list(map(int, input().split())))
answer = []
for x in range(n):
  i = 0
  j = n - 1
  while i < j:
    if i == x:
      i += 1
    elif j == x:
      j -= 1
    elif nums[i] + nums[j] < nums[x]:
      i += 1
    elif nums[i] + nums[j] > nums[x]:
      j -= 1
    elif nums[i] + nums[j] == nums[x]:
      answer.append(nums[x])
      break
print(len(answer))