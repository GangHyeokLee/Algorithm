from collections import deque

n = int(input())
m = int(input())

net = {}
for i in range(n+1):
  net[i] = []

for _ in range(m):
  a, b = map(int, input().split())
  
  a, b = min(a,b), max(a,b)
  
  net[a].append(b)

print(net)
que = deque()

que.append(1)

ans = 0

visited = [True] * (n+1)
while len(que):
  now = que.popleft()
  print(now, net[now], ans)
  for i in net[now]:
    if visited[i]:
      ans += 1
      visited[i] = False
      que.append(i)
      
print(ans)