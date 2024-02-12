import sys

input = sys.stdin.readline

from heapq import heappop, heappush

def show_result():
  print(len(result))
  for i in range(len(result)):
    print(result[i], end=' ')
    if (i+1) %10 == 0:
      print()

  print()


for _ in range(int(input())):
  m = int(input())
  data = []

  for i in range(m//10+1):
    data.extend(list(map(int, input().split())))

  left = []
  right = []
  median = data[0]
  result = [median]

  for i in range(1, m):
    if data[i] <= median: heappush(left, -data[i])
    else: heappush(right, data[i])

    if i%2 == 0:
      if len(left) > len(right):
        heappush(right, median)
        median = -heappop(left)
      elif len(left) < len(right):
        heappush(left, -median)
        median = heappop(right)
      result.append(median)
  show_result()