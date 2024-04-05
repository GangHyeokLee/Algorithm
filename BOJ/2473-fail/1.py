import sys
input = sys.stdin.readline

n = int(input())
liq = list(map(int, input().split()))
liq.sort()

# 두 가지 방향으로 가기 - 두 개 섞은 염기 + 하나 산
result = (6000000000, -1, -1, -1)

# 0인 조합 찾았는지 플래그
found = False
for i in range(n-2):
  if found:
    break
  start, end = i+1, n-1
  while start < end:
    sum = liq[i] + liq[start] + liq[end]
    
    if abs(sum) < abs(result[0]):
      result = (sum, liq[i], liq[start], liq[end])
    
    # 염기가 셈
    if sum < 0:
      start += 1
    elif sum > 0:
      end -= 1
    else: # 다 해서 0
      found = True
      break
    
print(*result[1:])