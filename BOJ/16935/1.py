n, m, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
operations = list(map(int, input().split()))

for op in operations:
  if op == 1:
    arr.reverse()
  if op == 2:
    for i in arr:
      i.reverse()
  if op == 3:
    newArr = [[0] * len(arr) for _ in range(len(arr[0]))]
    for i in range(len(arr[0])):
      for j in range(len(arr)-1, -1, -1):
        newArr[i][len(arr) -1 -j] = arr[j][i]
        
    arr = newArr
      
  if op == 4:
    newArr = [[0] * len(arr) for _ in range(len(arr[0]))]
    for i in range(len(arr[0])-1, -1, -1):
      for j in range(len(arr)):
        newArr[len(arr[0])-1-i][j] = arr[j][i]
    arr = newArr
  if op == 5:
    newArr = [[0] * len(arr[0]) for _ in range(len(arr))]
    dy, dx = len(arr)//2, len(arr[0])//2
    for i in range(len(arr)):
      for j in range(len(arr[0])):
        if i < len(arr)//2 and j < len(arr[0])//2: #1번 그룹
          newArr[i][j+dx] = arr[i][j]
          
        elif i < len(arr) // 2 and j >= len(arr[0])//2: #2번 그룹
          newArr[i+dy][j] = arr[i][j]
          
        elif i >= len(arr)//2 and j >= len(arr[0])//2: #3번 그룹
          newArr[i][j-len(arr[0])//2] = arr[i][j]
          
        elif i >= len(arr)//2 and j < len(arr[0])//2: #4번 그룹
          newArr[i-dy][j] = arr[i][j]
    arr = newArr
  if op == 6:
    newArr = [[0] * len(arr[0]) for _ in range(len(arr))]
    dy, dx = len(arr)//2, len(arr[0])//2
    for i in range(len(arr)):
      for j in range(len(arr[0])):
        if i < len(arr)//2 and j < len(arr[0])//2: #1번 그룹
          newArr[i+dy][j] = arr[i][j]
          
        elif i < len(arr) // 2 and j >= len(arr[0])//2: #2번 그룹
          newArr[i][j-dx] = arr[i][j]
          
        elif i >= len(arr)//2 and j >= len(arr[0])//2: #3번 그룹
          newArr[i-dy][j] = arr[i][j]
          
        elif i >= len(arr)//2 and j < len(arr[0])//2: #4번 그룹
          newArr[i][j+dx] = arr[i][j]
    arr = newArr
for k in arr:
  for j in k:
    print(j, end=" ")
  print()