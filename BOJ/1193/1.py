# 1 2 4 7 11
# x1 = 1
# xi = x(i-1) + i-1

n = int(input())
i = 1
xi = 1
while n > xi + i-1:
  i+=1
  xi = xi + i-1

if i%2 == 0:
  c, p = 1, i
  for i in range(xi, n):
    c += 1
    p -= 1
else:
  c, p = i, 1
  for i in range(xi, n):
    c -= 1
    p += 1
  
print(str(c) + "/" + str(p))