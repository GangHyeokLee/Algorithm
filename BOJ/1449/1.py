import sys

input = sys.stdin.readline

n, l = map(int, input().split())
leak = list(map(int, input().split()))

leak.sort()

l-=1
i=0

count = 0
while i < n:
  k = i
  while k < n and leak[k] <= leak[i] + l:
    k+=1
  count += 1
  i = k

print(count)