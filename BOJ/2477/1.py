from collections import deque
chamoe = int(input())
sero = deque()
garo = deque()
dirs = [0]*5

for _ in range(6):
  dir, length = map(int, input().split()) 
  dirs[dir]+=1  
  if dir in [3, 4]:    
    sero.append(length)  
  else:  
    garo.append(length)
garoM = max(garo)
seroM = max(sero)

# 가장 긴 길이 빼고 나머지 남기기
while garo[0] != garoM:  
  garo.append(garo.popleft())
while sero[0] != seroM:
  sero.append(sero.popleft())
garo.popleft()
sero.popleft()

# ㄱ 
if dirs[1] > dirs[2]:  
  #ㄱ  
  if dirs[3]>dirs[4]:  
    print((garoM * seroM - garo[0] * sero[1]) * chamoe)
  #┏  
  else:  
    print((garoM * seroM - garo[1] * sero[0]) * chamoe)
# ㄴelse:
  #ㄴ  
  if dirs[3]<dirs[4]: 
    print((garoM * seroM - garo[0] * sero[1]) * chamoe)
  # ┛  
  else:    
    print((garoM * seroM - garo[1] * sero[0]) * chamoe)