n, k = map(int, input().split())

comb = 1
for i in range(k):
  comb *= n - i


for i in range(k):
  comb //= i+1

print(comb%10007)