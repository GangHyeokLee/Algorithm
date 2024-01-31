N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))


A.sort()

h = [0]

for i in A:
  while len(h)<=i:
    h.append(0)
  
  h[i] = 1

for i in B:
  if i < len(h) and h[i]:
    print(1)
  else:
    print(0)