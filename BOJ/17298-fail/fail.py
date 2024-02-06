n = int(input())
arr = list(map(int, input().split()))

a = []
for x, i in enumerate(arr):
  a.append((x, i))

a.sort(key=lambda x:x[1])

ans = [-1] * n


print(a)