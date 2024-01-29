import sys

input = sys.stdin.readline

n = int(input())

ans = ""

stack = []
series = []

for i in range(n):
  series.append(int(input()))
  
j = 0
for i in range(1, n+1):
  stack.append(i)
  ans += "+"
  while stack and stack[-1] == series[j]:
    ans+="-"
    stack.pop()
    j+=1

if len(stack):
  print("NO")
else:
  for i in ans:
    print(i)