n = int(input())

fact = 1

for i in range(1, n+1):
  fact *= i

fact = str(fact)

ans = 0
for i in range(len(fact)-1, -1, -1):
  if fact[i] != '0':
    break
  ans += 1
print(ans)