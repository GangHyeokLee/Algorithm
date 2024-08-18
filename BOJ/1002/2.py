for _ in range(int(input())):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  
  dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  if x1 == x2 and y1 == y2 and r1 == r2:
    print(-1)
  elif r1 + r2 == dist or max(r2, r1) == min(r2, r1) + dist:
    print(1)  
  elif r1 + r2 > dist and max(r2, r1) < min(r1, r2) + dist:
    print(2)
  else:
    print(0)
  
  