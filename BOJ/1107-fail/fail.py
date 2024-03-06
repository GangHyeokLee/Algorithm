n = input()
m = int(input())

broken = list(map(int, input().split()))
buttons = [1] * 10
ans = 0

for i in broken:
  buttons[i] = 0

maxC = abs(int(n) - 100)

norIdx = -1
minstart = -1
maxstart = 10
for i in range(len(n)):
  ans += 1
  if buttons[int(n[i])] == 0:
    norIdx = i
    idx = int(n[i])
    for i in range(idx, -1, -1):
      if buttons[i] != 0:
        minstart = i
        break
    for i in range(idx + 1, 10):
      if buttons[i] != 0:
        maxstart = i
        break
    break

if norIdx != -1:
  done = int(n[:norIdx]) * (10 ** (len(n) - norIdx)) if norIdx > 0 else 0
  minstart = minstart * (10 ** (len(n) - norIdx - 1))
  maxstart = maxstart * (10 ** (len(n) - norIdx - 1))
  print(min([min([abs(int(n) - (done + minstart)), abs(int(n) - (done + maxstart))]) + ans, maxC]))
else:
  print(ans)
