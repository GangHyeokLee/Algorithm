n = int(input())

stars = []
for i in range(1, n):
  st = ""
  for j in range(i):
    st += "*"
  for j in range(n-i):
    st += " "
  ts = list(st)
  ts.reverse()
  st += "".join(ts)
  stars.append(st)
  print(st)
for i in range(2 * n):
  print("*", end="")
print()

stars.reverse()

for i in stars:
  print(i)