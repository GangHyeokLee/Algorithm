n = int(input())
seq = list(map(int, input().split()))
stack = []
ans = [-1] * n

for i in range(n-1, -1, -1):
  while stack:
    if stack[-1] <= seq[i]: #자기랑 작거나 같은 경우 제외시키기
      stack.pop()
    else:
      ans[i] = stack[-1]
      break
  stack.append(seq[i])
print(' '.join(map(str, ans)))