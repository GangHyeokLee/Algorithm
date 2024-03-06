n = int(input())
nums = list(map(int, input().split()))

seq = [1] * n

for i in range(n):
  for j in range(i):
    if nums[i] > nums[j]:
      seq[i] = max(seq[i], seq[j]+1)
      
print(max(seq))