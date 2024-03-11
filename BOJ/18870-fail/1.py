n = int(input())

nums = list(map(int, input().split()))

cord = {}

for i in nums:
  cord[i] = 1
    
arr = sorted(list(cord.items()))

cord[arr[0][0]] = 0
if len(arr) > 1:
  cord[arr[1][0]] = arr[0][1]

for i in range(2, len(arr)):
  cord[arr[i][0]] = cord[arr[i-1][0]] + arr[i-1][1]
  
for i in nums:
  print(cord[i], end=" ")