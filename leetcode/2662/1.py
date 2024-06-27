from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        point = set()
        point.add(tuple(start))
        point.add(tuple(target))

        for x1, y1, x2, y2, cost in specialRoads:
            graph[(x1, y1)].append(((x2, y2), cost))
            point.add((x1, y1))
            point.add((x2, y2))

        point = list(point)

        for i in point:
            for j in point:
                if i != j:
                    graph[i].append((j, abs(i[0]-j[0]) + abs(i[1]-j[1])))

        q = []
        heappush(q, (0, tuple(start)))
        dist = {tuple(start): 0}

        while q:
            cost, idx = heappop(q)

            if idx == tuple(target):
                return cost

            if idx in dist and dist[idx] < cost:
                continue

            for next, v in graph[idx]:
                if next not in dist or dist[next] > cost + v:
                    dist[next] = cost + v
                    heappush(q, (cost + v, next))
        return -1
