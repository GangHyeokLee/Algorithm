import sys
input = sys.stdin.readline

n, k = map(int, input().split())

temp = list(map(int, input().split()))

for i in range(1, n):
  temp[i] += temp[i-1]

ans = []
for i in range(k-1, n):
  if i - k >= 0:
    ans.append(temp[i] - temp[i-k])
  else:
    ans.append(temp[i])
    
print(max(ans))