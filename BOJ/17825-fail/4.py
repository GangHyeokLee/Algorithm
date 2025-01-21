nums = list(map(int, input().split()))

graph = dict()
blue = dict()

score = [
    0,
    2,
    4,
    6,
    8,
    10,
    13,
    16,
    19,
    25,
    12,
    14,
    16,
    18,
    20,
    22,
    24,
    22,
    24,
    26,
    28,
    30,
    32,
    34,
    36,
    38,
    26,
    27,
    28,
    30,
    35,
    40,
    0,
]

graph[0] = [1]
graph[1] = [2]
graph[2] = [3]
graph[3] = [4]
graph[4] = [5]
graph[5] = [10, 6]
graph[6] = [7]
graph[7] = [8]
graph[8] = [9]
graph[9] = [29]
graph[10] = [11]
graph[11] = [12]
graph[12] = [13]
graph[13] = [14]
graph[14] = [17, 15]
graph[15] = [16]
graph[16] = [9]
graph[17] = [18]
graph[18] = [19]
graph[19] = [20]
graph[20] = [21]
graph[21] = [22, 28]
graph[22] = [23]
graph[23] = [24]
graph[24] = [25]
graph[25] = [31]
graph[26] = [9]
graph[27] = [26]
graph[28] = [27]
graph[29] = [30]
graph[30] = [31]
graph[31] = [32]
graph[32] = [32]

ans = 0

horses = [0, 0, 0, 0]


def move(next, count):
    while count > 0 and next != 32:
        next = graph[next][0]
        count -= 1
    return next


def backtracking(horses, idx, s):
    global ans

    if idx == 10:
        ans = max(ans, s)
        return

    for i in range(4):
        count = nums[idx]
        now = horses[i]

        next = graph[now][-1]
        next = move(next, count - 1)

        if next not in horses or next == 32:
            nhorse = horses[:]
            nhorse[i] = next
            backtracking(nhorse, idx + 1, s + score[next])


backtracking(horses, 0, 0)

print(ans)
