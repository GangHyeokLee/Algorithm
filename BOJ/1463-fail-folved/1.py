n = int(input())
result = [0] * (n+1)

if n > 1:
  result[2] = 1
if n > 2:
  result[3] = 1
  
for i in range(4, n+1):
  case1 = i - 1
  case2 = i // 2 if i%2 == 0 else case1
  case3 = i // 3 if i%3 == 0 else case1
  result[i] = min(result[case1], result[case2], result[case3]) + 1
  
print(result[-1])