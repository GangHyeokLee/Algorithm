import sys
from heapq import heappop, heappush
input = sys.stdin.readline

for _ in range(int(input())):
  i=0
  maxheap = []
  minheap = []
  c = int(input())
  removed = [0] * c
  for _ in range(c):
    op, num = input().split()
    num = int(num)
    if op == 'I':
      heappush(minheap, (num, i))
      heappush(maxheap, (-num, i))
      i+=1
    elif op == 'D' and num == 1:
      if len(maxheap):
        x, idx = heappop(maxheap)
        while removed[idx] and len(maxheap):
          x, idx = heappop(maxheap)
        removed[idx] = 1
    else:
      if len(minheap):
        x, idx = heappop(minheap)
        while removed[idx] and len(minheap):
          x, idx = heappop(minheap)
        removed[idx] = 1

  if len(maxheap) and len(minheap):
    max, idx = heappop(maxheap)
    while removed[idx] and len(maxheap):
      max, idx = heappop(maxheap)

    min, idx = heappop(minheap)
    while removed[idx] and len(minheap):
      min, idx = heappop(minheap)
    
    print(-max, min)
    
  else:
    print('EMPTY')