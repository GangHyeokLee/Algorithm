import sys

sys.setrecursionlimit(10 ** 6)

def concat(operator):
  print(oper, len(oper))

  if len(oper) == n-1:
    result = str(nums[0])
    calc = str(nums[0])
    for i in range(1, n-1):
      if oper[i] == '+':
        result += '+'
        calc += '+'
      elif oper[i]  == '-':
        result += '-'
        calc+= '-'
      elif oper[i] == ' ':
        result += ' '
      result += str(nums[i+1])
      calc += str(nums[i+1])
      
    if eval(calc) == 0:
      ans.append(result)

    return

  oper.append(operator)

  concat(' ')
  oper.pop()

  concat('+')
  oper.pop()

  concat('-')
  oper.pop()


for _ in range(int(input())):
  n = int(input())
  nums = list(range(1, n+1))

  ans = []
  oper = []

  concat(' ')
  oper.pop()

  concat('+')
  oper.pop()

  concat('-')
  oper.pop()

  print(ans)