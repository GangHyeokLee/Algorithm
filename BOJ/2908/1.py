a, b = input().split()

a = list(a)
a.reverse()
a = int(''.join(a))

b = list(b)
b.reverse()
b = int(''.join(b))

print(a if a>b else b)