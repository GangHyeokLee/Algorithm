from bisect import bisect_left

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
nums = list(map(int, input().split()))

cards.sort()


ans = []
for i in nums:
  idx = bisect_left(cards, i)
  if idx < len(cards):
    ans.append(1 if i == cards[idx] else 0)

print(' '.join(map(str, ans)))
