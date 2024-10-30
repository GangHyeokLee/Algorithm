from collections import defaultdict

n = int(input())

friend = defaultdict(list)

while True:
  a, b = map(int, input().split())
  if a == -1 and b == -1:
    break
  
  friend[a].append(b)
  friend[b].append(a)
  

score = [100] * (n+1)
for i in range(1, n+1):
  que = [(i, 0)]
  idx = 0
  visited = [True] * (n+1)
  visited[i] = False
  
  while idx < len(que):
    now, count = que[idx]
    idx += 1
    
    for next in friend[now]:
      if visited[next]:
        visited[next] = False
        que.append((next, count+1))
  
  score[i] = max(que, key=lambda x: x[1])[1]

ans = min(score)
count = score.count(ans)
president = []
for idx, s in enumerate(score):
  if s == ans:
    president.append(idx)
    
print(ans, count)
print(" ".join(map(str, president)))