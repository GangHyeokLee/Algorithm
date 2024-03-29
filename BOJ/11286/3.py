import heapq as hq
import sys

input = sys.stdin.readline
max_heap = [] # 양수
min_heap = [] # 음수
for _ in range(int(input())):
  x = int(input())
  if x>0:
    hq.heappush(min_heap, x)
  elif x<0:
    hq.heappush(max_heap, -x)
  else:
    if min_heap:
      if max_heap:
        if min_heap[0] < abs(max_heap[0]):
          print(hq.heappop(min_heap))
        else:
          print(-hq.heappop(max_heap))
      else:
        print(hq.heappop(min_heap))
    else:
      if max_heap:
        print(-hq.heappop(max_heap))
      else:
        print(0)