n = int(input())

apart = []
for _ in range(n):
  apart.append(list(map(int, input().split())))

for i in range(n):
  for j in range(n):
    if apart[i][j] == 1:
      