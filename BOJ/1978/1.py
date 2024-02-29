import math

n = int(input())
nums = map(int, input().split())

ans = 0

for i in nums:
  chk = True
  
  if i == 1:
    continue
  
  if i==2:
    ans+=1
    continue
  
  for j in range(2, int(math.sqrt(i))+1):
    if i % j == 0:
      chk = False
  if chk:
    ans += 1
    
print(ans)