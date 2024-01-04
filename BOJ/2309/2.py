from itertools import combinations

heights = [int(input()) for _ in range(9)]

for combi in combinations(heights, 7):
  if sum(combi) == 100:
    for height in sorted(combi):
      print(height)
    break