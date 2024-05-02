sen = list(input())


opers = []
for s in sen:
  if ord(s) >= ord('A') and ord(s) <= ord('Z'):
    print(s, end="")
  else:
    
    if s == '(':
      opers.append(s)
    elif s == ')':
      while opers and opers[-1] != '(':
        print(opers.pop(), end="")
      opers.pop()
    elif s == '*' or s == '/':
      while opers and (opers[-1] == '*' or opers[-1] == '/'):
        print(opers.pop(), end="")
      opers.append(s)
    elif s == '+' or s == '-':
      while opers and opers[-1] != '(':
        print(opers.pop(), end="")
      opers.append(s)
    
while opers:
  print(opers.pop(), end="")
    
    
# a*(b+c*d) => abcd*+*

# a*(b*c+d*e) => abc*de*+*