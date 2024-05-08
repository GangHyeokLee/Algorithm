n = int(input())

sum = 0
i = 0
while sum < n:
  i += 1
  sum = i * (i+1) // 2
  
if sum == n:
  print(i)
else:
  print(i-1 if i > 1 else 1)