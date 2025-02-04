r1, c1, r2, c2 = map(int, input().split())

width = c2 - c1 + 1
height = r2 - r1 + 1
max_len = 0
nums = [[0] * width for _ in range(height)]

for i in range(height):
	for j in range(width):
		c = c1 + j
		r = r1 + i
		nsq = max(abs(c), abs(r))
		if c == 0 and r == 0:
			nums[i][j] = 1
		elif c == nsq and r != nsq: # 오른쪽 변, 
			nums[i][j] = (2 * nsq - 1) ** 2 + nsq * 2 * 0 + abs(nsq - r)
		elif r == -nsq and c != nsq: # 위쪽변
			nums[i][j] = (2 * nsq - 1) ** 2 + nsq * 2 * 1 + abs(nsq - c)
		elif c == -nsq and r != -nsq: # 왼쪽 변
			nums[i][j] = (2 * nsq - 1) ** 2 + nsq * 2 * 2 + abs(-nsq - r)
		elif r == nsq and c != -nsq: # 아래쪽변
			nums[i][j] = (2 * nsq - 1) ** 2 + nsq * 2 * 3 + abs(-nsq - c)

		max_len = max(max_len, len(str(nums[i][j])))

for n in nums:
	tmp = ""
	for l in n:
		for _ in range(max_len - len(str(l))):
			tmp += " "
		tmp += str(l) + " "
	print(tmp[:-1])
