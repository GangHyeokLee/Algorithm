import sys

input = sys.stdin.readline

m = int(input())
s = [0] * 21
for _ in range(m):
  order = list(input().split())
  
  if order[0] == 'add':
    s[int(order[1])] = 1
  elif order[0] == 'remove':
    s[int(order[1])] = 0
  elif order[0] == 'check':
    print(s[int(order[1])])
  elif order[0] == 'toggle':
    if s[int(order[1])]:
      s[int(order[1])] = 0
    else:
      s[int(order[1])] = 1
  elif order[0] == 'all':
    s = [1] * 21
  elif order[0] == 'empty':
    s = [0] * 21