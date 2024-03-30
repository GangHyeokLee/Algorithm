import sys
input = sys.stdin.readline

n = int(input())
l = int(input())
ios = input().strip()

i, pattern, ans = 0, 0, 0

while i + 2 < l:
  if ios[i:i+3] == "IOI":
    pattern += 1
    i+=2
  else:
    pattern = 0
    i+=1
  if pattern >= n:
    pattern -= 1
    ans += 1

print(ans)