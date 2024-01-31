import sys
input = sys.stdin.readline

for _ in range(int(input())):
  net = dict()
  for _ in range(int(input())):
    a, b = input().split()
    if a in net:
      net[a].add(b)
    else:
      net[a] = {b}

    if b in net:
      net[b].add(a)
    else:
      net[b] = {a}
  print(net)
