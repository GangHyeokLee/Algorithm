n = int(input())
liq = list(map(int, input().split()))

liq.sort()

start = 0
end = n-1
result = (2000000000, -1, n)

while start < end: 
  sum = liq[start] + liq[end]
  
  if abs(sum) < abs(result[0]):
    result = (sum, liq[start], liq[end])
  
  # 산성이 더 세니까 줄이기
  if sum > 0:
    end -= 1
  # 염기가 더 세니까 줄이기
  elif sum < 0:
    start += 1
  else:
    break
print(result[1], result[2])