n = int(input())

line = list(map(int, input().split()))

people = []

for i, v in enumerate(line):
  people.append((v, i))

people.sort()

ans = 0
for i in range(len(people)):
  ans += (len(people) - i) * people[i][0]
  
print(ans)