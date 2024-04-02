from collections import deque

n, m, r = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

ans = [[0]*m for _ in range(n)]

#한줄로 뽑아서 돌리기
def rotate(minY, minX, lenY, lenX):
  maxY, maxX = minY + lenY - 1, minX + lenX - 1
  tmp = deque()
  for i in range(minY, maxY): #아래
    tmp.append(arr[i][minX])
  for i in range(minX, maxX): #오른쪽
    tmp.append(arr[maxY][i])
  for i in range(maxY, minY, -1): #위
    tmp.append(arr[i][maxX])
  for i in range(maxX, minX, -1): #왼쪽
    tmp.append(arr[minY][i])
  for i in range(r):
    tmp.appendleft(tmp.pop())
  for i in range(minY, maxY):
    ans[i][minX] = tmp.popleft()
  for i in range(minX, maxX): #오른쪽
    ans[maxY][i] = tmp.popleft()
  for i in range(maxY, minY, -1): #위
    ans[i][maxX] = tmp.popleft()
  for i in range(maxX, minX, -1): #왼쪽
    ans[minY][i] = tmp.popleft()

  
for i in range(min(m, n)//2 - 1, -1, -1):
  rotate(i, i, n - 2*i, m-2*i)

for i in ans:
  for j in i:
    print(j, end=" ")
  print()