from collections import deque

cards = deque(range(1, int(input())+1))

while len(cards) > 1:
  cards.popleft()
  
  if len(cards)>1:
    cards.append(cards.popleft())
  else:
    break

print(cards[0])