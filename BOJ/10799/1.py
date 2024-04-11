from collections import deque

n = input()

ans = 0
stack = deque()
for i in range(len(n)):
  if stack and i > 0 and  n[i-1] == '(' and n[i] == ')':
    stack.pop()
    ans += len(stack)
  elif stack and i > 0 and n[i-1] == ')' and n[i] == ')':
    stack.popleft()
    ans += 1
  else:
    stack.append(i)
print(ans)