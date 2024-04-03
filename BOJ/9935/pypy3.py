# PyPy3 197156 420
import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()

ans = []
for i in string:
  ans.append(i)
  if len(ans) >= len(bomb):
    chk = True
    for i in range(len(bomb)):
      if ans[len(ans)-len(bomb)+i] != bomb[i]:
        chk = False
        
    if chk:
      for _ in range(len(bomb)):
        ans.pop()
        
print("".join(ans) if len(ans) else "FRULA")