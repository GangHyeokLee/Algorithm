n, r, c = map(int, input().split())


tmp = c
binc = 0

while tmp > 0:
  tmp = tmp // 2
  binc += 1

tmp = r

binr = 0
while tmp>0:
  tmp = tmp // 2
  binr += 1

print(binr, binc)
