import sys

input = sys.stdin.readline

n = int(input())

words = list(enumerate(list(input().strip() for _ in range(n))))
origin = words[:]
words.sort(key=lambda x:(x[1], x[0]))

maxCnt = 0
answer = (-1, -1)
pre = ""

for i in range(n-1):
    idx = 0
    cnt = 0

    ai, a = words[i]
    bi, b = words[i+1]

    if a == b:
        continue

    while idx < len(a) and i < len(b):
        if a[idx] == b[idx]:
            cnt += 1
        else:
            break
        idx += 1
    if maxCnt < cnt:
        maxCnt = cnt
        answer = (min(ai, bi), max(ai, bi))

pre = origin[answer[0]][1][:maxCnt]

printcount = 0
print1 = ""
for o in origin:
    if printcount == 2:
        break

    if o[1][:maxCnt] == pre and print1 != o[1]:    
        print(o[1])
        printcount += 1
        print1 = o[1]
