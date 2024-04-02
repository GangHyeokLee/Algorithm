ans = [-1, -1, -1]
for i in range(9):
  tmp = list(map(int, input().split()))
  newMax = max(tmp)
  if newMax > ans[0]:
    ans = [newMax, i, tmp.index(newMax)]
    
print(ans[0])
print(ans[1]+1, ans[2]+1)