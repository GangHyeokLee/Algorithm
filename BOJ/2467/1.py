n = int(input())

liq = list(map(int, input().split()))

start = 0
end = n-1

result = (2000000000, -1, n)

while start < end:
  mid = liq[start] + liq[end]
  
  if abs(mid) < abs(result[0]):
    result = (mid, liq[start], liq[end])
  
  # 염기가 세다
  if mid < 0:
    start += 1
  elif mid > 0:
    end -= 1
  else:
    break
print(result[1], result[2])