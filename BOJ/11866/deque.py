from collections import deque

n, k = map(int, input().split())

dq = deque(range(1, n+1))

ans = []

while len(dq) > 1:
  if len(dq) >= k:
    ans.append(dq[k-1])
    while dq[0] != ans[-1]:
      dq.append(dq.popleft())
  else:
    a = k % len(dq)
    ans.append(dq[a-1])
    while dq[0] != ans[-1]:
      dq.append(dq.popleft())
  dq.popleft()

ans.append(dq[0])



print('<', end="")
for i in range(len(ans)-1):
  print(ans[i], end=", ")

print(ans[-1], end=">")