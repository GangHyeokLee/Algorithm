import sys

input = sys.stdin.readline

ans = []

for _ in range(int(input())):
  a = list(map(int, input().split()))
  ans.append(a)


ans = sorted(ans)

for i in ans:
  print(i[0], i[1])