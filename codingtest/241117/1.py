from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    k -= 1
    s = deque(map(int, input().split()))
    samples = set()
    count = 0
    answer = -1
    while True:
        if len(set(s)) == 1:
            answer = count
            break

        if tuple(s) in samples:
            answer = -1
            break

        samples.add(tuple(s))

        s.append(s[k])
        s.popleft()
        count += 1

    print("#" + str(test_case), answer)
