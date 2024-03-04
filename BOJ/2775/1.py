t = int(input())

apart = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
for _ in range(t):
  k = int(input())
  n = int(input())
  
  if len(apart) > k:
    print(sum(apart[k-1][:n+1]))
  else:
    t = len(apart) - 1
    while t < k:
      floor = []
      for i in range(15):
        floor.append(sum(apart[t][:i+1]))
      apart.append(floor)
      t+=1
    print(apart[k][n])