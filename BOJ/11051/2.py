import sys
sys.setrecursionlimit(10 ** 7)

MOD = 10007

cache = [[0] * 1001 for _ in range(1001)]
N,K = map(int, input().split())

def bino(n, k):
  if cache[n][k]:
    return cache[n][k]

  if k==0 or k==n:
      return 1
  cache[n][k] = bino(n-1, k) + bino(n-1, k-1)
  return cache[n][k]

print(bino(N, K)%MOD)