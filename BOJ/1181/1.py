n = int(input())

words = set()
for _ in range(n):
  w = input()
  words.add((len(w), w))
  
words = list(words)
words.sort()

for i in words:
  print(i[1])