import sys
input = sys.stdin.readline

n = int(input())
sky = []

for _ in range(n):
  _, y = map(int, input().split())
  
  sky.append(y)
ans = 0
buildings = []
for i in sky:
  if not buildings or buildings[-1] < i:
    buildings.append(i)
  elif buildings[-1] > i:
    t = buildings.pop()
    ans += 1
    while buildings and buildings[-1] > i:
      if t > buildings[-1]:
        ans += 1
      t = buildings.pop()
      
    buildings.append(i)


if buildings:
  t = buildings.pop()
  if t != 0:
    ans += 1
  while buildings and buildings[-1] != 0:
    if t > buildings[-1]:
      ans += 1
    t = buildings.pop()


print(ans)