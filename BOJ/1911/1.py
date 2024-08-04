n, l = map(int, input().split())

need = [list(map(int, input().split())) for _ in range(n)]

need.sort()

left = need[0][0]
right = left + l - 1

ans = 1

for i in range(0, n):
  need[i][1] -= 1
  if right > need[i][1]:
    continue
  elif need[i][0] <= right < need[i][1]:
    dif = need[i][1] - right
    plates = dif // l + (1 if dif % l else 0)
    
    right += plates * l
    ans += plates
    
    
  elif right < need[i][0]:
    left = need[i][0]
    right = left + l - 1
    ans += 1
    if right < need[i][1]:
      dif = need[i][1] - right
      plates = dif // l + (1 if dif % l else 0)
    
      right += plates * l
      ans += plates
    
  
print(ans)