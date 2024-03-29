import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []

for _ in range(n):
  coins.append(int(input()))

coins.reverse()

count = 0

for i in coins:
  count += k // i
  k = k % i

print(count)