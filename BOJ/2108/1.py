import sys

input = sys.stdin.readline

n = int(input())

nums = []
num = {}

for i in range(n):
  data = int(input())
  nums.append(data)
  if data in num:
    num[data] += 1
  else:
    num[data] = 1
  
print(round(sum(nums)/n))

nums.sort()

print(nums[n//2])

max = max(num.values())
fre = []
for i, v in num.items():
  if v >= max:
    max = v
    fre.append(i)
    
fre.sort()
print(fre[1] if len(fre) > 1 else fre[0])
print(nums[-1] - nums[0])