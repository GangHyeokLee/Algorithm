import sys

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

cardsHash = {}

for i in cards:
  if i in cardsHash:
    cardsHash[i] += 1
  else:
    cardsHash[i] = 1
    
m = int(input())
chk = list(map(int, input().split()))

for i in chk:
  if i in cardsHash:
    print(cardsHash[i], end=" ")
  else:
    print(0, end=" ")