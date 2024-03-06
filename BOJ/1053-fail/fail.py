n = int(input())
nums = list(map(int, input().split()))

seq = []

for i in nums:
  for j in seq:
    if i > j[-1]:
      j.append(i)
  seq.append([i])
maxLen = 0
for j in seq:
  maxLen = max( len(j), maxLen)

print(maxLen)