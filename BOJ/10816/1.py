n = int(input())
ncards = list(map(int, input().split()))

m = int(input())
mcards = list(map(int, input().split()))

cardn = {}

for i in ncards:
  if i in cardn:
    cardn[i]+=1
  else:
    cardn[i] = 1
    
for i in mcards:
  if i in cardn:
    print(cardn[i], end = " ")
  else:
    print(0, end=" ")