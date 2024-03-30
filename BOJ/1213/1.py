from collections import defaultdict
name = input()

alpha = defaultdict(int)

for i in name:
  alpha[i]+=1

alphaItems = list(alpha.items())

alphaItems.sort()

ans = ""
mid = ""
chk = 0
for i in alphaItems:
  if i[1]%2:
    mid = i[0]
    chk+=1

  ans += i[0] * (i[1]//2)
  
ans += mid

alphaItems.reverse()
for i in alphaItems:
  ans += i[0] * (i[1]//2)
  
if chk > 1:
  print("I'm Sorry Hansoo")
else:
  print(ans)