import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

start = 0
end = max(t) * m
result = 0
while start <= end:
  mid = (start + end) // 2
  total = 0
  # mid 시간동안 각 심사대에서 심사 받을 수 있는 사람 수 전부 더하기
  for i in t:
    total += mid // i
  if total >= m:
    end = mid - 1
    result = mid
  else:
    start = mid + 1
    
print(result)