while True:
  sen = input()
  if sen == '.':
    break
  
  stack = 1
  r = 0
  s = 0
  done = True
  for i in sen:
    if i == "[":
      stack *= 101
      s+=1
    elif i == "]":
      s-=1
      if stack % 101 != 0 or s < 0:
        print('no')
        done = False
        break
      stack //= 101
      
    elif i == "(":
      stack += 1
      r += 1
    elif i == ")":
      r -= 1
      stack -= 1
      if stack <= 0 or s < 0:
        print('no')
        done = False
        break
      
  if done:
    if stack == 1 and s == 0 and r == 0:
      print('yes')
    else:
      print('no')