n, r, c = map(int, input().split())

def calz(n, r, c, index):
  if n == 1:
    return index
  # 좌상
  if 0 <= r < n // 2 and 0 <= c < n // 2:
    return calz(n // 2, r, c, index)
  
  # 우상
  if n//2 <= c < n and 0 <= r < n // 2:
    return calz(n // 2, r, c - n // 2, index + (n//2) ** 2)  
  #좌하
  if  0 <= c < n // 2 and n//2 <= r < n:
    return calz(n // 2, r - n // 2, c, index + (n//2) ** 2 * 2)
  
  #우하
  if  n//2 <= r < n and n//2 <= c < n:
    return calz(n // 2, r - n // 2, c - n // 2, index + (n//2) ** 2 * 3)
    
print(calz(2 ** n, r, c, 0))