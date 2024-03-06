n, k = map(int, input().split())

payload = []
maxValue = 0
for i in range(n):
  payload.append(list(map(int, input().split())))
  
payload.sort()

visited = [False] * n
def dfs(i, weight, value):
  global maxValue
  for j in range(i, n):
    if not visited[j]:
      visited[j] = True
      weight += payload[j][0]
      value += payload[j][1]
      if weight <= k:
        maxValue = max(maxValue, value)
        dfs(j, weight, value)
      weight -= payload[j][0]
      value -= payload[j][1]
      visited[j] = False
      
      
for i in range(n):
  visited[i] = True
  dfs(i, payload[i][0], payload[i][1])
print(maxValue)
