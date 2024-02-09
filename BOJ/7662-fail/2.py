import sys
input = sys.stdin.readline
import heapq

def pop(heap):
  while len(heap) > 0:
    data, id = heapq.heappop(heap)
    if not deleted[id]:
      deleted[id] = True
      return data
  return None

for _ in range(int(input())):
  k = int(input())

  min_heap = []
  max_heap = []
  current = 0
  deleted = [False] * (k+1)

  for i in range(k):
    command = input().split()
    operator, data = command[0], int(command[1])

    if operator == 'D':
      if data == -1: pop(min_heap)
      elif data == 1: pop(max_heap)
    elif operator == 'I':
      heapq.heappush(min_heap, (data, current))
      heapq.heappush(max_heap, (-data, current))
      current += 1
  max_value = pop(max_heap)
  if max_value == None: print('EMPTY')
  else:
    heapq.heappush(min_heap, (-max_value, current))
    print(-max_value, pop(min_heap))