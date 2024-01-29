from collections import deque

for i in range(int(input())):
  N, M = map(int, input().split())
  dq = deque(list(map(int, input().split())))
  count = 0
  i = 0
  while True:
    if M==0 and dq[M] == max(dq):
      print(count+1)
      break
    elif M==0:
      dq.append(dq.popleft())
      M = len(dq)-1
    elif dq[0] == max(dq):
      dq.popleft()
      count+=1
      M-=1
    else:
      dq.append(dq.popleft())
      M-=1

  