import sys

input = sys.stdin.readline

n, m = map(int, input().split())

hear = {}

for _ in range(n):
  hear[input().rstrip()] = False

for _ in range(m):
  see = input().rstrip()
  try:
    hear[see]
    hear[see] = True
  except:
    hear[see] = False

ans = []
for i in hear.items():
  if i[1]:
    ans.append(i[0])
    
ans.sort()

print(len(ans))
for i in ans:
  print(i)