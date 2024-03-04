import sys

input = sys.stdin.readline

n = int(input())

code = []
for _ in range(n):
  x, y = map(int, input().split())
  code.append((y, x))

code.sort()

for i in code:
  print(i[1], i[0])
  
