from collections import deque

n = int(input())

stairs = []

for _ in range(n):
  stairs.append(int(input()))
  
now = -1

que = deque()

que.append((-1, 0, 0))

ans = []

while que:
  now, score, concat = que.popleft()
  
  if now == n-1:
    ans.append(score)
    continue
  
  if concat < 1 and now + 1 < n:
    que.append((now + 1, score + stairs[now+1], concat + 1 if now >= 0 else concat))
  if now + 2 < n:
    que.append((now+2, score + stairs[now+2], 0))
    
print(max(ans))