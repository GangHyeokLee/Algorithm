n = int(input())

room_x = []

for _ in range(n):
  room_x.append(input())
  
room_y = []

for i in range(n):
  y = ""
  for j in range(n):
    y += room_x[j][i]
  room_y.append(list(y.split("X")))

x = 0
y = 0
for i in range(n):
  tmpx = list(room_x[i].split("X"))
  for t in tmpx:
    if len(t) >= 2:
      x+=1
  
  for t in room_y[i]:
    if len(t) >= 2:
      y+=1
      
print(x, y)