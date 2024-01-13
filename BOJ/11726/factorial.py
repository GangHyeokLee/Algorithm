import math

n = int(input())

ans = 0
for i in range(n // 2+1):
  ones = i*2 + n%2
  twos = n // 2 - i

  ans += math.factorial(ones+twos) / (math.factorial(twos) * math.factorial(ones))
    
print(int(ans%10007))
