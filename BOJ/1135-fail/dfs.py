from collections import defaultdict

n = int(input())
parent = list(map(int, input().split()))

company = defaultdict(list)

# Correct loop starting from 1 to properly handle root node 0
for i in range(1, n):
    company[parent[i]].append(i)
    


def dfs(e):
  
  if not company[e]:
    return 0
  
  times = []
  
  for child in company[e]:
    times.append(dfs(child))
  
  max_time = 0    
  times.sort(reverse=True)
  
  for i, t in enumerate(times):
    max_time = max(max_time, t + i + 1)
  return max_time

print(dfs(0))