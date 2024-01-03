import sys

input = sys.stdin.readline

n = int(input())

books = {}

for _ in range(n):
  book = input().rstrip()

  if book in books:
    books[book] += 1
  else:
    books[book] = 1

m = max(books.values())
answer = []
for k, v in books.items():
  if v == m:
    answer.append(k)

answer.sort()
print(answer[0])