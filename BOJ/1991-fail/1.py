from collections import deque
n = int(input())

tree = dict()

for _ in range(n):
  p, l, r = input().split()

  tree[p] = []

  if l != '.':
    tree[p].append(l)
  if r != '.':
    tree[p].append(r)

start = 'A'

deque = ['A']

