page = [input().split() for _ in range(10)]

papers = [0] * 6

for paper in range(5, 0, -1):
  for i in range(10 - paper + 1):
    for j in range(10 - paper + 1):
      if page[i][j] == '1':
        chk = False
        for x in range(0, paper):
          for y in range(0, paper):
            if page[i+x][j+y] != '1':
              chk = True
              break

          if chk:
            break
        
        if not chk:
          papers[paper]+=1
          for x in range(0, paper):
            for y in range(0, paper):
              page[i+x][j+y] = paper

chk = True
for i in range(5, 0, -1):

  if papers[1] > 5:
    print(-1)
    chk = False
    break

  rest = 0
  if papers[i] > 5:
    rest = papers[i] - 5
    papers[i] = 5

    if rest > 1:
      print(-1)
      chk = False
      break

    if i==5:
      papers[3]+=1
      papers[2]+=3
      papers[1]+=4
    elif i==4:
      papers[2] += 4
    elif i==3:
      papers[2] += 1
      papers[1] += 5
    elif i==2:
      papers[1] += 4

if chk:
  print(sum(papers))