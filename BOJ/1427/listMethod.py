n = input()

nums = []

for i in n:
  nums.append(int(i))

sorted_nums = []

for i in sorted(nums, reverse=True):
  sorted_nums.append(str(i))

print(''.join(sorted_nums))