t = int(input())


s = [0, 1, 2, 4]

def oneTwoThree(n):
  
  if len(s) > n:
    return s[n]
  
  s.append(oneTwoThree(n-1) + oneTwoThree(n-2) + oneTwoThree(n-3))
  return s[n]

for _ in range(t):
  n = int(input())
  print(oneTwoThree(n))