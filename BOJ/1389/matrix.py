N, M = map(int, input().split())

people = [[0] * (N+1) for _ in range(N+1)]
kevin = []

for _ in range(M):
  a, b = map(int, input().split())
  people[a][b] = 1
  people[b][a] = 1

for i in people:
  print(i)
  
  

