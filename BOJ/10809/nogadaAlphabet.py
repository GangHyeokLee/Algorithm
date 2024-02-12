s = input()

ans = [-1] * 26
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(s)):
  loc = alpha.index(s[i])
  if ans[loc] == -1:
    ans[loc] = i

for i in ans:
  print(i, end=' ')