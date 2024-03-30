import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
ds = list(map(int, input().split()))

chk = False
start = 0
end = a+b-1

while start <= end:
  mid = (start + end) // 2
  

print("Yes" if chk else "No")

def isItPossible(d):
  for i in ds:
    if 0 < (i+d) % (a+b) <= a:
      continue
    else:
      return False
  return True