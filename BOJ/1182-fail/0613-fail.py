n, s = map(int, input().split())

nums = list(map(int, input().split()))

ans = 0
def dfs(idx, sum):
  global ans
  if sum == s:
    ans += 1
  for i in range(idx + 1, n):
      dfs(i, sum + nums[i])
      
  return ans


for i in range(n):
  dfs(i, nums[i])

print(ans)