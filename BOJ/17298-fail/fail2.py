n = int(input())
arr = list(map(int, input().split()))

o = []
ans = [-1] * n

for i, x in enumerate(arr):
  if len(o) == 0 or o[-1][1] >= x:
    o.append((i, x))
  else:
    while len(o)>0:
      index, previous = o.pop()
      if previous >= x:
        o.append((index, previous))
        break
      else:
        ans[index] = x
    o.append((i, x))

for i in ans:
  print(i, end =" ")
