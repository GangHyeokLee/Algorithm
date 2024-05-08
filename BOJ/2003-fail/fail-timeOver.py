import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

seqsum = []

for s in seq:
  if seqsum:
    seqsum.append(seqsum[-1] + s)
  else:
    seqsum.append(s)
    
ans = 0
for j in range(0, n):
  for i in range(-1, j):
    if i >= 0:
      if seqsum[j] - seqsum[i] == m:
        ans += 1
    else:
      if seqsum[j] == m:
        ans += 1
    
print(ans)