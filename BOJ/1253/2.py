# 자기 자신을 제외한 다른 수로 구해야하는데 조합은 그것을 제외시키지 않음

from itertools import combinations

n = int(input())

nums = list(map(int, input().split()))

twos = set(sum(pair) for pair in combinations(nums, 2))

ans = 0

for num in nums:
    if num in twos:
        ans += 1

print(ans)
