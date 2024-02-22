n = int(input())

trophy = []
for _ in range(n):
  trophy.append(int(input()))


left = 0
max = 0
for i in range(0, n):
  if max < trophy[i]:
    max = trophy[i]
    left+=1

max = 0
right = 0
for i in range(n-1, -1, -1):
  if max < trophy[i]:
    max = trophy[i]
    right+=1

print(left)
print(right)
