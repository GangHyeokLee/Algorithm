import sys
input = sys.stdin.readline

from heapq import heappop, heappush

n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, cost = map(int, input().split())
  
  adj[a].append((b, cost))

start, end = map(int, input().split())

dist = [100000 * m] * (n+1)
before = [i for i in range(n+1)]

que = [(0, start)]
dist[start] = 0

while que:
  cost, now = heappop(que)
  
  if dist[now] < cost:
    continue
  
  for next, d in adj[now]:
    if dist[next] > cost + d:
      dist[next] = cost + d
      before[next] = now
      heappush(que, (dist[next], next))
      
print(dist[end])

now = end
course = [end]
while now != start:
  course.append(before[now])
  now = before[now]
  
print(len(course))
course.reverse()
for c in course:
  print(c, end=" ")