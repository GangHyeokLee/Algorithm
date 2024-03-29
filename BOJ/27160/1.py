import sys

input = sys.stdin.readline

cards = {
  'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0
}

for _ in range(int(input())):
  info, num = input().split()
  cards[info] += int(num)

chk = False
for k, v in cards.items():
  if v == 5:
    chk = True

if chk:
  print('YES')
else:
  print('NO')