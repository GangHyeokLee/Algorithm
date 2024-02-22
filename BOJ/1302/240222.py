n = int(input())

books = dict()
for _ in range(n):
  b = input()
  if b in books:
    books[b] += 1
  else:
    books[b] = 1

key = list(books.keys())

key.sort()

ans = [0, 0]
for i in key:
  if ans[0] < books[i]:
    ans = [books[i], i]
print(ans[1])