import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

v = int(input())

ans = 0

for i in nums:
  if i == v:
    ans+=1
print(ans)