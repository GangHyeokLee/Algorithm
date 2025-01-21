nums = list(map(int, input().split()))

# routes = [
#     [-1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
#     [10, 13, 16, 19, 25, 30, 35, 40, 0],
#     [20, 22, 24, 25, 30, 35, 40, 0],
#     [30, 28, 27, 26, 25, 30, 35, 40, 0],
# ]

routes = [
    [-1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0],
    [-1, 13, 16, 19, 25, 30, 35, 40, 0],
    [-1, 22, 24, 25, 30, 35, 40, 0],
    [-1, 28, 27, 26, 25, 30, 35, 40, 0],
]

blue = [5, 10, 15]


horse = [0, 0, 0, 0]
hr = [0, 0, 0, 0]
ans = 0


def backtracking(horse, idx, score):
    if idx == 10:
        global ans
        ans = max(ans, score)
        return

    for i in range(4):
        now = horse[i]
        route = routes[hr[i]]
        count = nums[idx]

        if route[now] == 0:
            continue
        next = min((now + count), len(route) - 1)

        chk = True
        for h in range(4):
            if i == h:
                continue
            if horse[h] == next and hr[i] == hr[h]:
                chk = False
                break
        if chk:
            horse[i] = next
            backtracking(horse, idx + 1, score + route[next])
            horse[i] = now

        if now in blue:
            original_hr = hr[i]
            r = blue.index(now) + 1
            hr[i] = r
            route = routes[hr[i]]

            chk = True
            for h in range(4):
                if i == h:
                    continue
                if horse[h] == next and hr[i] == hr[h]:
                    chk = False
                    break

            if chk:
                next = min((now + count), len(route) - 1)
                horse[i] = next
                backtracking(horse, idx + 1, score + route[next])
                horse[i] = now
            hr[i] = original_hr


backtracking(horse, 0, 0)
print(ans)
