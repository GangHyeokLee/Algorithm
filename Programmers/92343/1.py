def solution(info, edges):
    answer = [0]

    adj = [[] for _ in range(len(info))]

    for a, b in edges:
        adj[a].append(b)

    dfs(0, adj, info, 1, 0, answer, [])
    return answer[0]


def dfs(start, adj, info, sheep, wolves, answer, track):

    if wolves >= sheep:
        return -1
    answer[0] = max(answer[0], sheep)

    search = adj[start] + track
    visited = set()
    while search:
        next = search.pop()
        chk = dfs(
            next,
            adj,
            info,
            sheep + abs(info[next] - 1),
            wolves + info[next],
            answer,
            search,
        )
        if chk == -1 and next not in search and next not in visited:
            search.append(next)
            visited.add(next)

    search = adj[start] + track
    visited = set()
    while search:
        next = search.pop(0)
        chk = dfs(
            next,
            adj,
            info,
            sheep + abs(info[next] - 1),
            wolves + info[next],
            answer,
            search,
        )
        if chk == -1 and next not in search and next not in visited:
            search.append(next)
            visited.add(next)
