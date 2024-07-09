n = int(input())
start, end = map(int, input().split())

parent = [i for i in range(n+1)]

for _ in range(int(input())):
  p, c = map(int, input().split())
  
  parent[c] = p
count = 0
now = start

print()

found = False
while parent[now] != now:
  next = parent[now]
  print(now, next)
  count += 1
  if next == end:
    fount = True
    break
  
  now = next

if found:
  print(count)
else:
  count = 0
  now = end
  while parent[now] != now:
    next = parent[now]
    print(now, next)
    count += 1
    if next == start:
      found = True
      break
    now = next
  
  if found:
    print(count)
  else:
    print(-1)