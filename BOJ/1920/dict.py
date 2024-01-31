N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))


A.sort()

h = dict()

for i in A:
  if i in h:
    continue
  else:
    h[i] = True

for i in B:
  if i in h:
    print(1)
  else:
    print(0)