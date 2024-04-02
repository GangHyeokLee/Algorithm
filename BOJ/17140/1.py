from collections import defaultdict
r, c, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]
ans = 0
count = defaultdict(int)

while len(arr) < r or len(arr[0]) < c or arr[r-1][c-1] != K:
  y, x = len(arr), len(arr[0])
  maxLen = 0
  if y >= x: # R
    for i in range(y):
      count.clear()
      for j in arr[i]:
        if j:
          count[j]+=1
      tmp = []
      for k, v in count.items():
        tmp.append([v, k])
      tmp.sort()
      newRow = []
      for t in tmp:
        newRow.append(t[1])
        newRow.append(t[0])
      maxLen = max(maxLen, len(newRow))
      arr[i] = newRow
    for i in arr:
      if len(i) < maxLen:
        i += [0] * (min(100, maxLen) - len(i))
      elif len(i) > 100:
        i = i[:100]
      
  else: #C
    transposed = []
    for i in range(x):
      count.clear()
      for j in range(y):
        if arr[j][i]:
          count[arr[j][i]] += 1
      tmp = []
      for k, v in count.items():
        tmp.append([v, k])
      tmp.sort()
      newCol = []
      for t in tmp:
        newCol.append(t[1])
        newCol.append(t[0])
      maxLen = max(maxLen, len(newCol))
      transposed.append(newCol)
    for i in transposed:
      if len(i) < maxLen:
        i += [0] * (min(100, maxLen) - len(i))
      elif len(i) > 100:
        i = i[:100]
    #transposed 변환하기
    newArr = [[0] * len(transposed) for _ in range(len(transposed[0]))]
    for i in range(len(newArr)):
      for j in range(len(newArr[0])):
        newArr[i][j] = transposed[j][i]
    arr = newArr
  ans += 1  
  # print(ans, arr[r-1][c-1], K, arr[r-1][c-1] == K)
  # for i in arr:
  #   for j in i:
  #     print(j, end=" ")
  #   print()
    
  if ans > 100:
    break

print(ans if ans <= 100 else -1)