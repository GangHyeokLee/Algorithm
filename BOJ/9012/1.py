for _ in range(int(input())):
  paren = input()
  stack = 0
  for i in paren:
    if i == "(":
      stack += 1
    elif i == ")":
      stack -= 1
      if stack < 0:
        break
  if stack == 0:
    print("YES")
  else:
    print("NO")