import sys

input = sys.stdin.readline

event = []

for _ in range(int(input())):
  x, y = map(int, input().split())
  
  event.append((x, 'start'))
  event.append((y, 'end'))
  

event.sort(key = lambda x: (x[0], x[1] != 'start', x[1] == 'end'))


answer = 0

status = 0
start = 0
end = 0
for x, type in event:
  if type == 'start':
    if status == 0:
      start = x
    status += 1
  elif type == 'end':
    status -= 1
  
  if status == 0:
    answer += x - start

print(answer)