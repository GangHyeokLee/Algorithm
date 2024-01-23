N, M = map(int, input().split())

square = []

for _ in range(N):
  square.append(input())

ans = -1

for i in range(3, min(N+1, M+1)):
  for j in range(N):
    for k in range(M):
      chk = False
      if square[j][k] == '0':
        continue
      for l in range(1, i+1):
        for m in range(1, i+1):
          if j+l >= N or k+m >= M or square[j+l][k+m] == '0':
            chk = True
          break
        if chk:
          break
      if not chk:
        print(square[j], i)
        ans = max(ans, i)
    
    
print(ans * ans)
      

