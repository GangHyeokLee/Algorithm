import sys

input = sys.stdin.readline

dwarfs = []

for _ in range(9):
  dwarfs.append(int(input()))

dwarfs.sort()
found = False

for i in range(len(dwarfs)-1):
  if found:
    break
  for j in range(i+1, len(dwarfs)):
    if found:
      break

    sum = 0
    for k in range(len(dwarfs)):
      if k != i and k != j:
        sum+=dwarfs[k]

    if sum == 100:
      dwarfs = dwarfs[:j] + dwarfs[j+1:]
      dwarfs = dwarfs[:i] + dwarfs[i+1:]
      for d in dwarfs:
        print(d)

      found = True
      break