tc = int(input())

for _ in range(tc):
  l = input()

  left = []
  right = []

  for c in l:
    if c == '<':
      if len(left):
        right.append(left.pop())
    elif c == '>':
      if len(right):
        left.append(right.pop())
    elif c== '-':
      if len(left):
        left.pop()
    else:
      left.append(c)
  
  right.reverse()
  
  print(''.join(left +right))