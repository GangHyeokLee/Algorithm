from collections import defaultdict

def solution(k, n, reqs):
    answer = 0
    rest = n - k
    inter = defaultdict(list)
    wer = [1] * k

    for s, d, t in reqs:
        inter[t - 1].append((s, d))

    waitTime = calTime(inter, wer)
    target = 0
    while rest:
        for idx in range(k):
            wer[idx] += 1
            w = calTime(inter, wer)
            if sum(w) < sum(waitTime):
                waitTime = w
                target = idx
            wer[idx] -= 1

        wer[target] += 1
        rest -= 1

    return sum(waitTime)


def calTime(inter, wer):
    waitTime = [0] * len(wer)

    for t, cur in enumerate(wer):
        r = inter[t][:]
        idx = 0

        endTime = [0] * cur

        for now in r:
            if cur > 0:
                endTime[cur - 1] = r[idx][0] + r[idx][1]
                cur -= 1
            else:
                next, time = min(enumerate(endTime), key=lambda x: x[1])
                if time > now[0]:
                    waitTime[t] += time - now[0]
                    endTime[next] = time + now[1]
                else:
                    endTime[next] = sum(now)
            idx += 1

    return waitTime

solution(3, 5, [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]])