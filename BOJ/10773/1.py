import sys

input = sys.stdin.readline

stack = []

for _ in range(int(input())):
  n = int(input())
  if n:
    stack.append(n)
  else:
    if len(stack): stack.pop()
  
print(sum(stack))
