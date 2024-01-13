N = int(input())

cache = [0] * 1001

def f(n):
  if n == 1:
    return 1
  if n==2:
    return 2
  if not cache[n]:
    cache[n] = f(n-1) + f(n-2)
  return cache[n]

print(f(N)%10007)
