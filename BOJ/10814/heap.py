import sys
import heapq

input = sys.stdin.readline

member = []

for i in range(int(input())):
  age, name = input().split()
  age = int(age)
  heapq.heappush(member, (age, i, name))

while len(member):
  mem = heapq.heappop(member)

  print(mem[0], mem[2])

