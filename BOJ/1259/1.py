while True:
  n = input()
  
  if n == '0':
    break
  
  front = n[:len(n)//2]
  back = n[len(n)//2 if len(n)%2==0 else len(n)//2+1:]
  
  chk = True
  for i in range(len(front)):
    if front[i] != back[-1+i]:
      print('no')
      chk = False
      break
  if chk: print('yes')