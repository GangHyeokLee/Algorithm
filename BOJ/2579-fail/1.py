n = int(input())

stairs = []

for _ in range(n):
  stairs.append(int(input()))
  
steps = [0] * 400
steps[0] = stairs[0]
if n > 1:
  steps[1] = max(stairs[1], stairs[0] + stairs[1])
if n > 2:
  steps[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
  steps[i] = max(steps[i-3] + stairs[i-1] + stairs[i], steps[i-2] + stairs[i])
  

print(steps[n-1])