for _ in range(int(input())):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  
  a = 2 * (x1 - x2)
  b = 2 * (y1 - y2)
  c = x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2 - r1 ** 2 + r2 ** 2
  
  if y1 != y2:
    count = 0
    for x in range(-10000, 10001):
      y = (a * x + c) / b
      if (x-x1) ** 2 + (y-y1) ** 2 == r1 ** 2 and (x-x2) ** 2 + (y - y2) ** 2 == r2 **2:
        count += 1
        if count > 2:
          count = -1
          break
    
  else:
    x = (r1 ** 2 - r2 ** 2 + x2 ** 2 - x1 ** 2) / 2 * (x2 - x1)
    
    if r1 ** 2 < (x - x1) ** 2:
      count = -1
    elif ( r1 ** 2 - (x-x1) ** 2) ** 0.5 - int(( r1 ** 2 - (x-x1) ** 2) ** 0.5) == 0:
      count = 1
    else:
      count = 2
    
    
    
    
        
  print(count)