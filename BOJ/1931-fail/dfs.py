import sys

inpuy = sys.stdin.readline

n = int(input())

con = []

for _ in range(n):
  con.append(list(map(int, input().split())))
  
con.sort()

ans = -1
visited = [True] * len(con)
def dfs(idx, plan):
  global ans
  for i in range(idx+1, n):
    if visited[i] and con[idx][1] <= con[i][0]:
      visited[i] = False
      plan.append(con[i])
      dfs(i, plan)
      plan.pop()
      visited[i] = True
  if len(plan) > ans:
    ans = len(plan)
    
for i in range(n):
  visited[i] = False
  dfs(i, [con[i]])
  visited[i] = True
  
print(ans)