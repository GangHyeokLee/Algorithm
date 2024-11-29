import sys

input = sys.stdin.readline

n = int(input())

sen = [input().strip() for _ in range(n)]

for s in sen:
  l = len(s)
  start = 0
  end = l - 1
  
  counta = 0
  while start <= end:
    if counta > 1:
      break
    
    if s[start] == s[end]:
      start += 1
      end -= 1
    elif start+1 <= end and s[start+1] == s[end]:
      start += 1
      counta += 1
    elif start <= end - 1 and s[start] == s[end - 1]:
      end -= 1
      counta += 1
    else:
      counta = 2
      
  start = 0
  end = l - 1
  countb = 0
  while start <= end:
    if countb > 1:
      break
    if s[start] == s[end]:
      start += 1
      end -= 1
    elif start <= end - 1 and s[start] == s[end - 1]:
      end -= 1
      countb += 1
    elif start+1 <= end and s[start+1] == s[end]:
      start += 1
      countb += 1
    else:
      countb = 2
      
    
  
  if counta == countb == 2:
    print(2)
  elif counta * countb == 2 or counta * countb == 1:
    print(1)
  else:
    print(0)