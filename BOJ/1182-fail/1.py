n, s = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

def dfs(idx, seq):
  global ans
  if sum(seq) == s:
    ans += 1
  
  for i in range(idx+1, n):
    seq.append(nums[i])
    dfs(i, seq)
    seq.pop()

for i in range(n):
  dfs(i, [nums[i]])
print(ans)