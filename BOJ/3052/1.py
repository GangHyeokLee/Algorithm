import sys

input = sys.stdin.readline

mod = []

for _ in range(10):
  mod.append(int(input())%42)

diff = set(mod)

print(len(diff))