import sys

input = sys.stdin.readline

stack = []

for _ in range(int(input())):
  line = input().split()
  order = ""
  num = 0
  if len(line) > 1:
    order, num = line
    num = int(num)
  else:
    order = line[0]

  if num:
    num = int(num)

  if order == 'push':
    stack.append(num)
  elif order == 'pop':
    print(stack.pop() if stack else -1)
  elif order == 'size':
    print(len(stack))
  elif order == 'empty':
    print(0 if stack else 1)
  elif order == 'top':
    print(stack[-1] if stack else -1)