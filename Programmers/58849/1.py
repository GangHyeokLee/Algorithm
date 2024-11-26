def solution(cap, n, deliveries, pickups):
    answer = 0

    d = []
    p = []
    for i in range(n):
        if deliveries[i]:
            d.append((i + 1, deliveries[i]))

        if pickups[i]:
            p.append((i + 1, pickups[i]))

    while d or p:
        next = max(d[-1][0] if d else 0, p[-1][0] if p else 0)

        answer += next * 2

        pos = cap

        while pos > 0 and d:
            idx, now = d.pop()
            if now - pos > 0:
                d.append((idx, now - pos))
            pos -= now

        pos = cap
        while pos > 0 and p:
            idx, now = p.pop()
            if now - pos > 0:
                p.append((idx, now - pos))
            pos -= now

    return answer