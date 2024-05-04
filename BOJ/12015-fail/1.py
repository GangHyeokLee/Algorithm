n = int(input())

seq = list(map(int, input().split()))

ans = [seq[0]]

for s in seq:
  if s > ans[-1]:
    ans.append(s)
  else:
    start = 0
    end = len(ans)
    
    while start < end:
      mid = (start + end) // 2
      if ans[mid] < s:
        start = mid + 1
      else:
        end = mid
    ans[end] = s
print(len(ans))