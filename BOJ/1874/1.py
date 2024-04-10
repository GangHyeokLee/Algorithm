import sys
input = sys.stdin.readline

n = int(input())

seq = [int(input()) for _ in range(n)]

stack = []
idx = 0
ans = []
for i in range(1, n+1):
  ans.append('+')
  stack.append(i)
  
  while stack and stack[-1] == seq[idx]:
    stack.pop()
    idx += 1
    ans.append('-')

if stack:
  print("NO")
else:
  for a in ans:
    print(a)