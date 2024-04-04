import sys
from heapq import heappush, heappop

input = sys.stdin.readline

for _ in range(int(input())):
  # 최대, 최소힙 두 개 유지
  maxheap = []
  minheap = []
  # 삭제 기록 유지 용 사전과 id
  deleted = {}
  id = 0
  for _ in range(int(input())):
    order, number = input().split()
    if order == 'I':
      heappush(minheap, (int(number), id))
      heappush(maxheap,(-int(number), id))
      id += 1
      # 새로 들어와서 삭제 기록 제거
    elif number == '1': # 최대값 빼기
      target = None
      # 삭제 기록에 없는 숫자 나올 때까지
      while maxheap:
        tmp = heappop(maxheap)
        if tmp[1] not in deleted:
          target = tmp
          break
      # 삭제 기록 남기기
      if target:
        deleted[target[1]] = True
    elif number == '-1':
      target = None
      # 삭제 기록에 없는 숫자 나올 때까지
      while minheap:
        tmp = heappop(minheap)
        if tmp[1] not in deleted:
          target = tmp
          break
      # 삭제 기록 남기기
      if target:
        deleted[target[1]] = True
  M = None
  # 삭제 기록에 없는 숫자 나올 때까지
  while maxheap:
    tmp = heappop(maxheap)
    if tmp[1] not in deleted:
      M = tmp
      break
  
  m = None
  while minheap:
    tmp = heappop(minheap)
    if tmp[1] not in deleted:
      m = tmp
      break
  if M and m:
    print(-M[0], m[0])
  else:
    print('EMPTY')