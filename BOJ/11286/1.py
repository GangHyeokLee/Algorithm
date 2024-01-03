import sys

n = int(sys.stdin.readline().rstrip())

print(n)

inte = []
absinte = []

for _ in range(n):
  i = int(sys.stdin.readline().rstrip())
  if i == 0:
    if len(inte)==0:
      print(0)
      continue
    absmin = min(absinte)
    idx = -1
    if -absmin in inte:
      idx = inte.index(-absmin)
    elif absmin in inte:
      idx = inte.index(absmin)
    
    if idx >=0:
      print(inte[idx])
      inte = inte[:idx] + inte[idx+1:]
      absinte = absinte[:idx] + absinte[idx+1:]

  else:
    inte.append(i)
    absinte.append(abs(i))
