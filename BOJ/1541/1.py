code = list(input().split('-'))

for i in range(len(code)):
  tmp = code[i].split('+')
  s = 0
  for j in tmp:
    s += int(j)
  code[i] = s

ans = code[0]

for i in range(1, len(code)):
  ans -= code[i]
  
print(ans)