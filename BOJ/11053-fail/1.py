n = int(input())

seq = list(map(int, input().split()))

next = [1] * n

ans = 0

for i in range(n):
  for j in range(i+1, n):
    if seq[i] < seq[j]:
      next[j] = max(next[j], next[i] + 1)
      
print(max(next))