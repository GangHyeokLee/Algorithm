n = int(input())

square = []

for _ in range(n):
  square.append(list(map(int, input().split())))


white = 0
blue = 0

def findBlue(startX, startY, l): # 시작점, 길이
  global white, blue
  
  chk = 0
  for i in range(startY, startY + l):
    chk += sum(square[i][startX:startX+l])
    
  if chk == 0:
    white += 1
    return
  elif chk == l * l:
    blue += 1
    return
  
  findBlue(startX, startY, l // 2)
  findBlue(startX + l//2, startY, l // 2)
  findBlue(startX, startY + l//2, l // 2)
  findBlue(startX + l//2, startY + l//2, l // 2)

findBlue(0, 0, n)

print(white)
print(blue)