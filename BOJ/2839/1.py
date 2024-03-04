n = int(input())

f = n // 5
fl = n % 5

while fl % 3 and f > 0:
  f -= 1
  fl += 5

if fl%3:
  print(-1)
else:
  print(f + fl//3)