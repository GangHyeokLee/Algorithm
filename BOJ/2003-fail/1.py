import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))

sum = seq[0]
left = 0
right = 1
ans = 0

while True:
  if sum < m:
    if right < n:
      sum += seq[right]
      right += 1
    else:
      break
  else:
    if sum == m:
      ans += 1
    sum -= seq[left]
    left += 1

print(ans)