import sys

input = sys.stdin.readline

n, b = input().split()

ans = 0
for i in range(len(n)):
  if n[len(n)-1-i].isdigit():
    ans += int(n[len(n)-1-i]) * (int(b) ** i)
  else:
    ans += (ord(n[len(n)-1-i]) - 55) * (int(b) ** i)
    
print(ans)