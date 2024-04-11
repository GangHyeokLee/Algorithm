import sys

input = sys.stdin.readline

n, s = map(int, input().split())

seq = list(map(int, input().split()))

start = 0
end = 0
ans = 1000000

tmp = seq[0]

while start <= end and end < n:
  if tmp < s:
    end += 1
    if end < n:
      tmp += seq[end]
  else:
    ans = min(ans, end-start + 1)
    tmp -= seq[start]
    start += 1
    

print(ans if ans < 1000000 else 0)