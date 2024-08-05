n, d, k, c = map(int, input().split())

sushi = [int(input()) for _ in range(n)]

eat = set()

ans = 0
for i in range(n):
  if i + k <= n:
    eat = set(sushi[i:i+k])
  else:
    eat = set(sushi[i:] + sushi[:(i+k)%n])
  
  eat.add(c)
  ans = max(ans, len(eat))
  
print(ans)