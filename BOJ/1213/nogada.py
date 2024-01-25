name = input()

alpha = [[] for _ in range(26)]

for i in name:
  if i=='A':
    alpha[0].append(i)
  elif i=='B':
    alpha[1].append(i)
  elif i=='C':
    alpha[2].append(i)
  elif i=='D':
    alpha[3].append(i)
  elif i=='E':
    alpha[4].append(i)
  elif i=='F':
    alpha[5].append(i)
  elif i=='G':
    alpha[6].append(i)
  elif i=='H':
    alpha[7].append(i)
  elif i=='I':
    alpha[8].append(i)
  elif i=='J':
    alpha[9].append(i)
  elif i=='K':
    alpha[10].append(i)
  elif i=='L':
    alpha[11].append(i)
  elif i=='M':
    alpha[12].append(i)
  elif i=='N':
    alpha[13].append(i)
  elif i=='O':
    alpha[14].append(i)
  elif i=='P':
    alpha[15].append(i)
  elif i=='Q':
    alpha[16].append(i)
  elif i=='R':
    alpha[17].append(i)
  elif i=='R':
    alpha[17].append(i)
  elif i=='R':
    alpha[17].append(i)
  elif i=='L':
    alpha[11].append(i)
  elif i=='M':
    alpha[12].append(i)
  elif i=='N':
    alpha[13].append(i)
  elif i=='O':
    alpha[14].append(i)
  elif i=='P':
    alpha[15].append(i)
  elif i=='Q':
    alpha[16].append(i)
  elif i=='R':
    alpha[17].append(i)
  elif i=='S':
    alpha[18].append(i)
  elif i=='T':
    alpha[19].append(i)
  elif i=='U':
    alpha[20].append(i)
  elif i=='V':
    alpha[21].append(i)
  elif i=='W':
    alpha[22].append(i)
  elif i=='X':
    alpha[23].append(i)
  elif i=='Y':
    alpha[24].append(i)
  elif i=='Z':
    alpha[25].append(i)


odd = 0
length = 0
center = ""
for i in alpha:
  length+=len(i)
  if len(i)%2:
    center = i.pop()
    odd+=1

if odd > 1:
  print("I'm Sorry Hansoo")
else:
  ans = ""
  for i in alpha:
    if i:
      if len(ans) == length//2:
        ans += center
        break
      else:
        for j in range(len(i)//2):
          ans+=i.pop()
  
  if len(ans) == length//2:
      ans += center

  for i in range(len(alpha)-1, -1, -1):
    if alpha[i]:
      for j in alpha[i]:
        ans+=j

  print(ans)