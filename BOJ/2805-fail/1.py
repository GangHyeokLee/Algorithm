n, m = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()

start = 0
end = trees[-1]

while start <= end:
  mid = (start + end) // 2
  total = 0
  for i in trees:
    total += (i - mid) if i > mid else 0
  
  if total >= m:
    start = mid + 1
  elif  total < m:
    end = mid - 1
    
print(end)