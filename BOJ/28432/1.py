words = []
q = -1
for i in range(int(input())):
  words.append(input())
  if words[-1] == "?":
    q = i
  
bq = words[q-1][-1] if q-1 >= 0 else ""
aq = words[q+1][0] if q+1 < len(words) else ""

ans = ""
for _ in range(int(input())):
  i = input()
  if not ans and len(words) == 1:
    ans = i
  if i in words:
    continue
  if i[0] == bq and i[-1] == aq:
    ans = i
  elif not aq and bq and bq == i[0]:
    ans = i
  elif not bq and aq and aq == i[-1]:
    ans = i
    
print(ans)