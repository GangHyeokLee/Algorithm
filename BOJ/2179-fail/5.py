n = int(input())

words = [input() for _ in range(n)]

swords = sorted(enumerate(words), key=lambda x: x[1])

ans = [0, 2000001, 2000001]

for i in range(n - 1):
    ai, a = swords[i]
    bi, b = swords[i + 1]
    count = 0
    for idx in range(min(len(a), len(b))):
        if a[idx] == b[idx]:
            count = idx + 1
            continue
        break

    if count > ans[0]:
        ans = [count, min(ai, bi), max(ai, bi)]
    elif count == ans[0]:
        if ans[1] > min(ai, bi):
            ans = [count, min(ai, bi), max(ai, bi)]
        elif ans[1] == min(ai, bi) and ans[2] > max(ai, bi):
            ans = [count, min(ai, bi), max(ai, bi)]

pre = words[ans[1]][: ans[0]]
answer = []
for word in words:
    if len(answer) == 2:
        break
    if word.startswith(pre) and word not in answer:
        answer.append(word)

print("\n".join(answer))
