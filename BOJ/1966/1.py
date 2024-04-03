from collections import deque

printer = deque()

for _ in range(int(input())):
  n, m = map(int, input().split())
  docs = deque(map(int, input().split()))
  order = deque(range(n))
  count = 0
  
  while docs:
    mx = max(docs)
    while mx != docs[0]:
      docs.append(docs.popleft())
      order.append(order.popleft())
    if order[0] == m:
      print(count+1)
      break
    docs.popleft()
    order.popleft()
    count+=1