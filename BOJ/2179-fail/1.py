import sys
input = sys.stdin.readline

n = int(input())

ip = []
for i in range(n):
  ip.append((input().strip(), i))
  
  
words = sorted(ip)

ans = [0] * (n)
maxCnt = 0
for i in range(n-1):
    cnt = 0
    a = words[i][0]
    b = words[i+1][0]
    
    for x in range(min(len(a), len(b))):
      if a[x] == b[x]:
        cnt += 1
      else:
        break
    maxCnt = max(cnt, maxCnt)
    
    ans[words[i][1]] = max(ans[words[i][1]], cnt)
    ans[words[i+1][1]] = max(ans[words[i+1][1]], cnt)

chk = -1
pre = ""
for i in range(n):
  if chk == -1 and ans[i] == maxCnt:
    chk = i
    print(ip[i][0])
    pre = ip[i][0][:maxCnt]
  elif ans[i] == maxCnt and (maxCnt == 0 or pre == ip[i][0][:maxCnt]):
    print(ip[i][0])
    break
    