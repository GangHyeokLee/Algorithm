from heapq import heappop, heappush

n, m = map(int, input().split())
cards = []
for c in map(int, input().split()):
  heappush(cards, c)

for i in range(m):
  # 가장 작은 값 두 개 꺼내기
  a = heappop(cards)
  b = heappop(cards)
  
  # 둘이 더한 값 넣기
  heappush(cards, a+b)
  heappush(cards, a+b)
print(sum(cards))