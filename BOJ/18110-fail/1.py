import sys

input = sys.stdin.readline

n = int(input())

oper = []

for i in range(n):
  oper.append(int(input()))
  
oper.sort()

cut = n * 0.15
rest = cut - cut // 1
cut = int(cut)
if rest >= 0.5:
  cut += 1

refinedOper = oper[cut:n-cut]

if n == 0:
  print(0)
else:
  ans = sum(refinedOper) // len(refinedOper)
  rest = sum(refinedOper) / len(refinedOper) - ans
  
  if rest >= 0.5:
    print(ans+1)
  else:
    print(ans)