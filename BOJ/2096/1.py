n = int(input())

minDp = [[10, 10, 10] for _ in range(2)]
maxDp = [[-1, -1, -1] for _ in range(2)]

# minDp[n][0] = min(minDp[n-1][0] + table[n][0], minDp[n-1][1] + table[n][0])
for i in range(n):
  row = list(map(int, input().split()))
  
  minDp[i%2] = row.copy()
  maxDp[i%2] = row.copy()
  if i > 0:
    minDp[i%2][0] = min(minDp[abs(i%2-1)][:2]) + row[0]
    minDp[i%2][1] = min(minDp[abs(i%2-1)]) + row[1]
    minDp[i%2][2] = min(minDp[abs(i%2-1)][1:]) + row[2]
    
    maxDp[i%2][0] = max(maxDp[abs(i%2-1)][:2]) + row[0]
    maxDp[i%2][1] = max(maxDp[abs(i%2-1)]) + row[1]
    maxDp[i%2][2] = max(maxDp[abs(i%2-1)][1:]) + row[2]
  
print(max(maxDp[(n-1)%2]), min(minDp[(n-1)%2]))