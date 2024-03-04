while True:
  sen = input()
  if sen == '.':
    break
  
  stack = []
  chk = False
  for i in sen:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if len(stack) and stack[-1] == '(':
        stack.pop()
      else:
        chk = True
        break
    elif i == ']':
      if len(stack) and stack[-1] == '[':
        stack.pop()
      else:
        chk = True
        break
      
  if len(stack) or chk:
    print('no')
  else:
    print('yes')