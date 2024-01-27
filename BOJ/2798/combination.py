from itertools import combinations

N, M = map(int, input().split())

cards = list(map(int, input().split()))

comb = list(combinations(cards, 3))

ans = 0
for i in comb:
  if M-sum(i)>=0 and M - ans > M - sum(i):
    ans = sum(i)

print(ans)