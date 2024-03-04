import heapq
import sys

input = sys.stdin.readline

n = int(input())

cards = []

for _ in range(n):
  heapq.heappush(cards, int(input()))
  


ans = 0
while len(cards)>1:
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  
  ans += a+b
  
  heapq.heappush(cards, a+b)
  
print(ans)