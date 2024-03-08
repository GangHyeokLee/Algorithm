import sys

inpuy = sys.stdin.readline

n = int(input())

con = []

for _ in range(n):
  con.append(list(map(int, input().split())))
  
con.sort(key=lambda x:(x[1], x[0]))

ans = 0
end = 0
for s, e in con:
  if end <= s:
    ans += 1
    end = e
print(ans)