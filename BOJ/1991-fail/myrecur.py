from collections import deque
n = int(input())

tree = dict()

for _ in range(n):
  p, l, r = input().split()

  tree[p] = []

  
  tree[p].append(l)
  
  tree[p].append(r)

start = 'A'

order = deque()

def preorder(parent):
  if len(order) == 0:
    order.append(parent)
  [l, r] = tree[parent]

  if l != '.':
    order.append(l)
    preorder(l)
  
  if r != '.':
    order.append(r)
    preorder(r)

preorder('A')
for i in order:
  print(i, end="")

print()
order.clear()

def midorder(parent):
  [l, r] = tree[parent]
  if l != '.':
    midorder(l)
  
  order.append(parent)

  if r != '.':
    midorder(r)

midorder('A')
for i in order:
  print(i, end="")

print()
order.clear()

def postorder(parent):
  [l, r] = tree[parent]
  if l != '.':
    postorder(l)
  if r != '.':
    postorder(r)
  order.append(parent)


postorder('A')
for i in order:
  print(i, end="")

print()
order.clear()