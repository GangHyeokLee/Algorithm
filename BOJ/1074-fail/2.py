n, r, c = map(int, input().split())

ans = 0
while n > 0:
  n -= 1
  if r < 2 ** n and c < 2 ** n:
    ans += 0
  
  elif c >= 2 ** n and r < 2 ** n:
    ans += (2 ** (n*2) ) * 1
    c -= 2 ** n
    
  elif c < 2 ** n and r >= 2 ** n:
    ans += (2 ** (n*2) ) * 2
    r -= 2 ** n
  
  elif c >= 2 ** n and r >= 2 ** n:
    ans += (2 ** (n*2) ) * 3
    c -= 2 ** n
    r -= 2 ** n

print(ans)