cords = list(map(int, input().split()))

ans = ""

for i in range(len(cords)-1):
  if ans=="ascending" and cords[i] - cords[i+1] > 0:
    ans = "mixed"
    break
  elif ans == "descending" and cords[i] - cords[i+1] <0:
    ans = "mixed"
    break
  elif cords[i] - cords[i+1] > 0:
    ans = "descending"
  elif cords[i] - cords[i+1] < 0:
    ans = "ascending"

print(ans)