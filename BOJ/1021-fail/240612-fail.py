import sys
from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))

que = deque([i for i in range(1, n+1)])

count = 0

for t in target:
  index = que.index(t)
  
  if index <= len(que) // 2:
    for i in range(index):
      que.append(que.popleft())
      count += 1
  else:
    for i in range(len(que) - index):
      que.appendleft(que.pop())
      count += 1
  que.popleft()
print(count)