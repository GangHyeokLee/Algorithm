a, b, c = map(int, input().split())

s = [0] * 81

for  i in range(1, a+1):
  for j in range(1, b+1):
    for k in range(1, c+1):
      s[i+j+k]+=1

max = [0, 0]

for i, v in enumerate(s):
  if max[1] < v:
    max = [i, v]

print(max[0])