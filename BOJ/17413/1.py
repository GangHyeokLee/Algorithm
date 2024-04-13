import sys
input = sys.stdin.readline

s = input().strip()

reverse = []
notReverse = []
i=0

ans = ""
while i < len(s):
  if s[i] == '<':
    
    ans += "".join(reversed(reverse))
    reverse.clear()
    
    while s[i] != '>':
      notReverse.append(s[i])
      i+=1
    notReverse.append(s[i])
    i+=1
    
    ans += "".join(notReverse)
    notReverse.clear()
  elif s[i] == " ":
    ans += "".join(reversed(reverse))
    reverse.clear()
    ans += s[i]
    i+=1
  else:
    reverse.append(s[i])
    i+=1

ans += "".join(reversed(reverse))
print(ans)