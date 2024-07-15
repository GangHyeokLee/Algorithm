n = int(input())
m = int(input())

ingre = sorted(list(map(int, input().split())))


min = 0
max = n - 1
answer = 0

while min < max:
  if ingre[min] + ingre[max] < m:
    min += 1
  elif ingre[min] + ingre[max] > m:
    max -= 1
  else:
    min += 1
    max -= 1
    answer+=1
    
print(answer)