import sys

input = sys.stdin.readline
chat = {}
ans = 0

for _ in range(int(input())):
  name = input().strip()
  if name == "ENTER":
    chat.clear()
  else:
    try:
      chat[name]+=1
    except:
      ans +=1
      chat[name] = 1

print(ans)