n = input()
m = input()

ans = 0
i=0
while i < len(n):
  chk = False
  next = i + len(m)
  for j in range(len(m)):
    if i+j >= len(n):
      chk = True
      break
    if n[i+j] != m[j]:
      chk = True
      break

  if not chk:
    ans += 1
    while i < next:
      i+=1
    continue
  i+=1


print(ans)