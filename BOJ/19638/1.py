# 가장 가치가 큰? max heap
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n, h, t = map(int, input().split())

giant = []
cnt = 0

for _ in range(n):
  heappush(giant, -int(input()))
  
for _ in range(t):
  g = -heappop(giant)
  #최소로 쓰기 위해 h이상일 때만 사용
  if g > 1 and g >= h: 
    heappush(giant, -(g//2))
    cnt += 1
  # 1은 그대로 다시 넣어주기
  else:
    heappush(giant, -g)

maxGiant = -heappop(giant)
if maxGiant >= h:
  print("NO")
  print(maxGiant)
else:
  print("YES")
  print(cnt)