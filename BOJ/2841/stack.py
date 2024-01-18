import sys

input = sys.stdin.readline

N, P = map(int, input().split())

strings = [[] for _ in range(7)]

ans = 0

for _ in range(N):
  n, p = map(int, input().split())
  if not strings[n] or strings[n][-1] < p:
    strings[n].append(p)
    ans+=1
  elif strings[n][-1] > p:
    while len(strings[n]) and strings[n][-1] > p:
      strings[n].pop()
      ans+=1
    if not strings[n] or strings[n][-1] < p:
      strings[n].append(p)
      ans+=1
print(ans)
