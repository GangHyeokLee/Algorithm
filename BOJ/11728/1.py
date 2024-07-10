n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = a+b
print(' '.join(map(str, sorted(a))))

# i = j = 0

# answer = [0] * (m+n)

# while i < n and j < m:
#   if a[i] <= b[j]:
#     answer[i+j] = a[i]
#     i+=1
#   else:
#     answer[i+j] = b[j]
#     j+=1

# for x in range(i, n):
#   answer[x+j] = a[x]

# for x in range(j, m):
#   answer[i+x] = b[x]

# print(' '.join(map(str, answer)))
