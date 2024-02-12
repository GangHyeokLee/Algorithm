import sys
from heapq import heappop, heappush

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  length = int(input())
  if length%10:
    length=length//10 + 1
  else:
    length = length//10

  nums = []
  for i in range(length):
    nums+=list(map(int, input().split()))

  middleNum = []
  heap = []

  for i in nums:
    heappush(heap, i)

    if len(heap)%2:
      middle = len(heap)//2
      temp = []
      for i in range(middle):
        temp.append(heappop(heap))

      middleNum.append(heappop(heap))

      heappush(heap, middleNum[-1])

      for i in temp:
        heappush(heap, i)

  cnt = 0
  print(len(middleNum))
  for i in middleNum:
    if cnt == 9:
      print(i)
      cnt = 0
    else:
      print(i, end=' ')
      cnt+=1
  print()

