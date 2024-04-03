import sys

input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))

ans = [0] * n
receiver = [[0, 0]]

for i, v in enumerate(tops):
  while receiver:
    if receiver[-1][1] < v:
      receiver.pop()
    else:
      ans[i] = receiver[-1][0] + 1
      break
  receiver.append((i, v))

print(" ".join(map(str, ans)))