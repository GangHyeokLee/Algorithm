a, b = map(int, input().split())

A = a//100 + ((a % 100) // 10) * 10 + (a % 10) * 100
B = b//100 + ((b % 100) // 10) * 10 + (b % 10) * 100

print(A if A > B else B)