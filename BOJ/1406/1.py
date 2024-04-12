import sys
input = sys.stdin.readline

# 커서 기준 왼쪽 오른쪽
left = list(input().strip())
right = list()

for i in range(int(input())):
  order = list(input().split())
  
  if order[0] == 'P':
    left.append(order[1])
  elif order[0] == 'L' and left:
    right.append(left.pop())
  elif order[0] == 'D' and right:
    left.append(right.pop())
  elif order[0] == 'B' and left:
    left.pop()
left.reverse()
while left:
  print(left.pop(), end = "")
while right:
  print(right.pop(), end = "")