n, k = map(int, input().split())

maxValue = 0
package = [[0] * (k+1) for i in range(n+1)]

for i in range(n):
  w, v = map(int, input().split())
  
  for j in range(1, k+1):
    if j >= w:
      package[i+1][j] = max(v + package[i][j - w], package[i][j])
    else:
      package[i+1][j] = package[i][j]
print(package[-1][-1])