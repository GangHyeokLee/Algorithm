import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
  heappush(cards, int(input()) )

ans = 0
while len(cards) > 1:
  a = heappop(cards)
  b = heappop(cards)
  ans += a+b
  heappush(cards, a+b)
  
print(ans)