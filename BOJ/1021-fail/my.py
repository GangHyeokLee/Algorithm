from collections import deque

n, m = map(int, input().split())

dq = deque(range(1, n+1))

t = list(map(int, input().split()))

ans = 0

for i in t:
  if dq[0] == i:
    dq.popleft()
  elif dq.index(i) < len(dq)//2 + 1 :
    while dq[0] != i:
      dq.append(dq.popleft())
      ans+=1
    dq.popleft()
  else:
    while dq[0]!=i:
      dq.appendleft(dq.pop())
      ans+=1
    dq.popleft()

print(ans)
  

