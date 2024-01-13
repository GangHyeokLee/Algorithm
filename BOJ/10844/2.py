MOD = 1_000_000_000

N = int(input())

# f(n) = 길이 n인 계단 수의 개수
# f(n, d) = f(n-1) ...

# 45656
# n=5
# 7 or 5

# 4565432101

# 7898

# f(n, d) = 길이가 n이고 마지막 숫자가 d인 계단수의 개수
# d: 0~9

# f(N, 0) + f(n, 1) + ... + f(n,9) % MOD

# f(n, d) = f(n-1, d-1) + f(n-1, d+1) 


# f(1) = 9

cache = [[0] * 10 for _ in range(101)]

for j in range(1, 10):
  cache[1][j] = 1

for i in range(2, 101):
  for j in range(10):
    if j>0:
      cache[i][j] += cache[i-1][j-1]
      cache[i][j] %= MOD
    if j < 9:
      cache[i][j] += cache[i-1][j+1]
      cache[i][j] %= MOD

ans = 0
for j in range(10):
  ans += cache[N][j]
  ans %= MOD

print(ans)