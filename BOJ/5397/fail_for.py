tc = int(input())

for _ in range(tc):
  l = input()

  pw = []
  i = -1
  for c in l:
    if c == '<':
      if  i >= 0:
        i-=1
    elif c == '>':
      if  i < len(l):
        i+=1
    elif c== '-':
      pw = pw[:i-1] + pw[i:]
    else:
      if i==-1:
        pw = [c] + pw
        i=0
      elif i == len(l):
        pw.append(c)
        i+=1
      else:
        pw = pw[:i+1] + [c] + pw[i+1:]
        i+=1

  print(''.join(pw))
    
