T = int(input())
for test_case in range(1, T + 1):
    answer = -20000 * 5000
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    sums = list(sum(s[i:i + k]) for i in range(n - k + 1))

    for a in range(n - 2 * k + 1):
        for c in range(a + k, n - k + 1):
            answer = max(answer, sums[a] + sums[c])

    print("#" + str(test_case), answer)
