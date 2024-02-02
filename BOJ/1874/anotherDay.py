import sys

input = sys.stdin.readline

i=1
ans = []
stack = []
for _ in range(int(input())):
  m = int(input())
  while i <= m:
    stack.append(i)
    ans.append('+')
    i+=1
  if stack[-1] == m:
    stack.pop()
    ans.append('-')

if len(stack):
  print('NO')
else:
  print('\n'.join(ans))