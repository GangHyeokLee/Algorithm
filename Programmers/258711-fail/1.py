from collections import defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    
    ine = defaultdict(list)
    oute = defaultdict(list)
    nodes = set()
    
    for a, b in edges:
        oute[a].append(b)
        ine[b].append(a)
        nodes.add(a)
        nodes.add(b)
    
    # 추가한 정점에서 다른 그래프로 향하는 간선들, 최소 두 개의 그래프 => 추가한 정점은 최소 두 개 이상의 나가는 간선만 있음
    target = None
    for n in nodes:
        if not ine[n] and len(oute[n]) >= 2:
            target = n
    
    # 나가는 간선과 연결된 정점을 기준으로 탐색 시작하기
    roots = oute[target]
    answer[0] = target
    
    for r in roots:
        answer[chkType(oute, ine, r)] += 1
        
    return answer

# 모든 노드가 out 하나 in하나이고 사이클이면 도넛 사이클이 아니면 막대, 정점 하나가 in2, out2면 8자
def chkType(oute, ine, root):
    type = 2 # 1: 도넛, 2: 막대, 3: 8
    que = [root]
    idx = 0
    visited = set()
    visited.add(root)
    
    while idx < len(que):
        now = que[idx]
        idx += 1
        
        if len(oute[now]) + len(ine[now]) >= 4:
            return 3
        
        for next in oute[now]:
            if next in visited:
                type = 1
            else:
                que.append(next)
                visited.add(next)
    return type     