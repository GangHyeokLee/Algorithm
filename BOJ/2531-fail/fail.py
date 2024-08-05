n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]


start = -1
dif = -1
ans = -1

ns = []
for i, v in enumerate(sushi):
  if v == c:
    ns = sushi[i:] + sushi[:i]
    break

for i, v in enumerate(ns):
  if v == c:
    if start != -1 and i - start >= k:
      print(i, start)
      ans = k + 1
    start = i
    
  if i == n-1 and start == 0:
    ans = k + 1
if ans == -1:
  print(k)
else:
  print(ans)