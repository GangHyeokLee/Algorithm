import sys

input = sys.stdin.readline

k, n = map(int, input().split())

cables = []

for _ in range(k):
  cables.append(int(input()))

max = max(cables)
min = 1

while min <= max:
  mid = (max + min) // 2
  
  total = 0
  for i in cables:
    total += i // mid
    
  if total < n:
    max = mid - 1
  elif total >= n:
    min = mid + 1

print(max)