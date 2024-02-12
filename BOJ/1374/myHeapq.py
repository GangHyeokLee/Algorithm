import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

lectures = []
end = []

for _ in range(n):
  lectures.append(list(map(int, input().split())))
  

lectures.sort(key=(lambda x:x[1]))

for i in lectures:
  if len(end)==0 or i[1] < end[0]:
    heappush(end, i[2])
  else:
    heappop(end)
    heappush(end, i[2])

print(len(end))