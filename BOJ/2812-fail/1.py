import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 길이가 n-k인 부분 수열 중 가장 큰 것?
nums = list(map(int, input().strip()))

ans = []

for i in nums:
  while ans and i > ans[-1] and k > 0:
    ans.pop()
    k -= 1
  ans.append(i)
  
while k:
  ans.pop()
  k-=1

print("".join(map(str, ans)))