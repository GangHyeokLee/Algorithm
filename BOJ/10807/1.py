n = int(input())

nums = {}
ns = list(map(int, input().split()))

for number in ns:
    if number in nums:
        nums[number] += 1
    else:
        nums[number] = 1
t = int(input())

print(nums[t] if t in nums else 0)