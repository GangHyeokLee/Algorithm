from itertools import permutations

n, m = map(int, input().split())

nums = list(range(1, n+1))

ans = list(permutations(nums, m))

for i in ans:
  for j in i:
    print(j, end=" ")
  print()