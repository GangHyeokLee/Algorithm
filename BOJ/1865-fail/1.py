for _ in range(int(input())):
  n, m, w = map(int, input().split())
  
  edges = []
  for _ in range(m):
    s, e, c = map(int, input().split())
    edges.append((c, s, e))
    edges.append((c, e, s))
    
  for _ in range(w):
    s, e, c = map(int, input().split())
    edges.append((-c, s, e))
    
  dp = [0] * (n+1)
  
  chk = False
  for i in range(1, n+1):
    for c, s, e in edges:
      if dp[s] + c >= dp[e]: continue
      dp[e] = dp[s] + c
      if i == n:
        chk = True
        
  print("YES" if chk else "NO")