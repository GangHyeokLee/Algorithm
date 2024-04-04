n = int(input())
nums = [int(input()) for _ in range(n)]

# x + y = k - z and x, y, z, k in nums
xy = []
ans = 0
for i in nums:
  for j in nums:
    xy.append(i+j)
xy = list(set(xy))
xy.sort()
for z in range(n):
  for k in range(z, n):
    kz = nums[k] - nums[z]
    start = z
    end = len(xy) - 1
    while start <= end:
      mid = (start + end) // 2
      if xy[mid] < kz:
        start = mid + 1
      elif xy[mid] > kz:
        end = mid - 1
      else:
        ans = max(ans, nums[k])
        break
print(ans)