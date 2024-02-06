n, k = map(int, input().split())

q = list(range(1, n+1))

ans = []

while len(q) > 1:
  if len(q) >= k:
    ans.append(q[k-1])
    q = q[k:] + q[:k-1]
  else:
    a = k % len(q)
    ans.append(q[a-1])
    q = q[a:] + q[:a-1]

ans.append(q[0])



print('<', end="")
for i in range(len(ans)-1):
  print(ans[i], end=", ")

print(ans[-1], end=">")