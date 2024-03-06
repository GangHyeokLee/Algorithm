n = int(input())

# 길이가 n인 수열 개수는
# n-1인 수열 개수 + n-2인 수열의 개수

def seq(n):
  
  if n == 1:
    return 1
  if n == 2:
    return 2
  
  return seq(n-1) + seq(n-2)

print(seq(n))