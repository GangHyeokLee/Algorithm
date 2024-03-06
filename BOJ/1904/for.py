n = int(input())

# 길이가 n인 수열 개수는
# n-1인 수열 개수 + n-2인 수열의 개수

sequence = [0] * n
sequence[0] = 1

if n > 1:
  sequence[1] = 2

for i in range(2, n):
  sequence[i] = sequence[i-1]%15746 + sequence[i-2]%15746
  
print(sequence[-1]%15746)