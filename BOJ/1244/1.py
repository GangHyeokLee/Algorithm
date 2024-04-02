n = int(input())
switches = list(map(int, input().split()))

c = int(input())
for i in range(c):
  s, t = map(int, input().split())
  if s == 1:
    for i in range(n):
      if (i+1) % t == 0:
        switches[i] = abs(switches[i] - 1)
  if s == 2:
    t-=1
    i=0
    while t - i >= 0 and t + i < n:
      if switches[t-i] != switches[t+i]:
        break
      i+=1
    i-=1
    for k in range(t-i, t+i+1):
      switches[k] = abs(switches[k]-1)
      
for i in range(n):
  print(switches[i], end=" ")
  if (i+1) %20 == 0:
    print()