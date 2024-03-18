import sys

input = sys.stdin.readline

k = int(input())

money = []
for _ in range(k):
  now = int(input())
  if now == 0:
    money.pop()
  else:
    money.append(now)
    
print(sum(money))