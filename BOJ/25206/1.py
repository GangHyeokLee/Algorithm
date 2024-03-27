n = 20

total = 0

score = {
  'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
}

total_score = 0

for i in range(n):
  lec = input().split()
  if lec[2] == 'P':
    continue
  total += float(lec[1])
  total_score += float(lec[1]) * float(score[lec[2]])
print(total_score/total)