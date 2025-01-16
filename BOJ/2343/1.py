n, m = map(int, input().split())

# 이진탐색인듯

lectures = list(map(int, input().split()))

start = max(lectures)

end = sum(lectures)
answer = 0

while start <= end:
    mid = (start + end) // 2

    count = 1
    sum = 0
    for l in lectures:
        if sum + l > mid:
            count += 1
            sum = 0
        sum += l
    if count > m:
        start = mid + 1
    else:
        answer = mid
        end = mid - 1

print(answer)
