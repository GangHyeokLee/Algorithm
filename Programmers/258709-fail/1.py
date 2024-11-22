from itertools import combinations, product


def solution(dice):
    answer = []
    # 전체 경기 수는 같고
    # 그럼 최대 승리 경우인 조합을 찾아야됨

    cases = list(combinations(range(len(dice)), len(dice) // 2))

    nums = list(product(range(6), repeat=len(dice) // 2))

    score = dict()
    for i, case in enumerate(cases):
        score[i] = []

        for n in nums:
            tmp = 0
            for idx, d in enumerate(n):
                tmp += dice[case[idx]][d]

            score[i].append(tmp)

        score[i].sort()

    ans = [0, -1]
    for a in range(len(cases)):
        b = len(cases) - a - 1
        tmp = 0
        for sa in score[a]:
            start = 0
            end = len(score[b]) - 1
            while start <= end:
                mid = (start + end) // 2

                if score[b][mid] >= sa:
                    end = mid - 1
                else:
                    start = mid + 1
            tmp += start
        if tmp > ans[0]:
            ans = [tmp, a]

    ans = list(cases[ans[1]])

    for a in range(len(ans)):
        ans[a] += 1
    return ans