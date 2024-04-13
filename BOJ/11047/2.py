n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]
ans = 0
for i in range(n-1, -1, -1):
  ans += k // coin[i]
  k %= coin[i]
print(ans)