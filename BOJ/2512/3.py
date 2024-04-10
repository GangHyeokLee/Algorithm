n = int(input())
bud = list(map(int, input().split()))

total = int(input())

start = 0
end = max(bud)
ans = 0

while start <= end:
  mid = (start + end) // 2
  
  # mid 기준으로 배정 예산 계산
  tmp = 0
  for i in bud:
    if i < mid:
      tmp += i
    else:
      tmp += mid
  
  if tmp > total:
    end = mid - 1
  else:
    ans = mid
    start = mid + 1
    
print(ans)