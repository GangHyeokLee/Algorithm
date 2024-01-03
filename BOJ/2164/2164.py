n = int(input())

cards = [x for x in range(n)]

i = 0

while i < len(cards):
  i+=1
  
  if i+1 < len(cards):
    cards.append(cards[i])
    i+=1
  else:
    break

print(cards[-1]+1)
  

