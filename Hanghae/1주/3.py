import sys

input = sys.stdin.readline

n = int(input())

tree = {}

for _ in range(n):
  p, l, r = input().split()
  
  tree[p] = [l, r]

def preOrder(p):
  [left, right] = tree[p]
  print(p, end="")
  if left != '.':
    preOrder(left)
  if right != '.':
    preOrder(right)
    
preOrder('A')
print()

def inOrder(p):
  [left, right] = tree[p]
  if left != '.':
    inOrder(left)
  print(p, end="")
  if right != '.':
    inOrder(right)
    
inOrder('A')
print()

def postOrder(p):
  [left, right] = tree[p]
  if left != '.':
    postOrder(left)
  if right != '.':
    postOrder(right)
  print(p, end="")
  
postOrder('A')
print()