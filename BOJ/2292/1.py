n = int(input())

i = 1
ni = 1
while ni < n:
  ni = ni + 6 * (i-1)
  i+=1
print(i-1 if i > 1 else 1)