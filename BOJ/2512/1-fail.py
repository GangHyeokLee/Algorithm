from bisect import bisect_left, bisect_right
import math

n = int(input())
budget = list(map(int, input().split()))
total = int(input())
budget.sort()

if sum(budget) > total:
  middle = math.ceil(total/n)
  print(middle)
  idx = bisect_left(budget, middle, 0, n-1)

  high_avg = sum(budget[idx:])/(n-idx)

  diff = (sum(budget) - total)/(n-idx)

  print(math.floor(high_avg-diff))

else:
  print(budget[-1])
