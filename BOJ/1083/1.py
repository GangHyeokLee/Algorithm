n = int(input())
arr = list(map(int, input().split()))
s = int(input())

idx = 0
while s > 0 and idx < n:
  localMax = max(arr[idx:min(idx + s + 1, n)])
  target = arr.index(localMax)
  
  for i in range(target, idx, -1):
    if s == 0:
      break
    arr[i], arr[i-1] = arr[i-1], arr[i]
    s -= 1
  idx += 1

print(' '.join(map(str,arr)))