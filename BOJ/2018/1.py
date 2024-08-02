n = int(input())

start = 0
end = 1
sum = 1
ans = 0

while start < end and end <= n:
  
  if sum <= n:
    if sum == n:
      ans += 1
    end += 1
    sum += end
    
  elif sum > n:
    start += 1
    sum -= start

print(ans)