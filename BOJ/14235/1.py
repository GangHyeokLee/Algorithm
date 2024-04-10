# 가장 가치가 큰? max heap
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
  check = list(map(int, input().split()))
  
  if len(check) == 1 and check[0] == 0: #거점지 아닌 곳 방문
    print(-heappop(heap) if heap else -1)
  else:
    for i in range(check[0]):
      heappush(heap, -check[i+1])