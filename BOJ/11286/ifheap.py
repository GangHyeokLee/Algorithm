from heapq import heappop, heappush
import sys

input = sys.stdin.readline

pos = []
neg = []

for _ in range(int(input())):
  x = int(input())

  if x > 0:
    heappush(pos, x)
  elif x < 0:
    heappush(neg, abs(x))
  else:
    if len(pos) == 0 and len(neg) == 0:
      print(0)
    elif len(pos)==0 or (len(neg) != 0 and pos[0] >= neg[0]):
      print(heappop(neg) * -1)
    elif len(neg)==0 or (len(pos) != 0 and pos[0] < neg[0]):
      print(heappop(pos))