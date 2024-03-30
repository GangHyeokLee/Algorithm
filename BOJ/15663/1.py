from itertools import permutations

n, m = map(int, input().split())
nums = list(permutations(map(int, input().split()), m))

nums = list(set(nums))
nums.sort()


for i in nums:
  for j in i:
    print(j, end=" ")
  print()