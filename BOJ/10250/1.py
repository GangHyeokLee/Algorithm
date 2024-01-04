import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  h, w, count = map(int, input().split())

  f = count % h

  if f==0:
    f = h
    r = count // h
  else:
    r = count // h + 1

  print(f*100 + r)