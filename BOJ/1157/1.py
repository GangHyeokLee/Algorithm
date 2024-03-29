s = input().upper()
alpha = {}
for i in s:
  if i in alpha:
    alpha[i] += 1
  else:
    alpha[i] = 1

m = max(alpha.values())

ans = []
for k, v in alpha.items():
  if v == m:
    ans.append(k)
    
if len(ans)==1:
  print(ans[0])
else:
  print('?')