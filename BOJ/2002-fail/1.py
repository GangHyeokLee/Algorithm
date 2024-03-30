n = int(input())
cars = {}

for i in range(n):
  cars[input()] = i
  
out = [input() for _ in range(n)]

ans = 0
for i in range(n-1):
  for j in range(i+1, n):
    if cars[out[i]] > cars[out[j]]:
      ans += 1
      break
    
print(ans)