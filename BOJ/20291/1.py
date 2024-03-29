import sys

input = sys.stdin.readline

files = {}

for _ in range(int(input())):
  _, t = input().strip().split('.')
  
  if t in files:
    files[t] += 1
  else:
    files[t] = 1
    
ans = list(files.items())

ans.sort()
for i in ans:
  print(i[0], i[1])