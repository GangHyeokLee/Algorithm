import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()

ans = []
for i in string:
  ans.append(i)
  if len(ans) >= len(bomb):
    if ''.join(ans[len(ans)-len(bomb):]) == bomb:
      for _ in range(len(bomb)):
        ans.pop()
        
print("".join(ans) if len(ans) else "FRULA")