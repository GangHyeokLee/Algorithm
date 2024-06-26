from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        dist = [-1] * n
        dist[0] = 0

        graph = defaultdict(list)

        for e in edges:
            u, v, length = e
            graph[u].append((v, length))
            graph[v].append((u, length))

        q = [(0, 0)]
        cost = 0

        while q:
            cost, idx = heappop(q)

            if 0 <= dist[idx] < cost:
                continue

            for adj, d in graph[idx]:        
                if (dist[adj] == -1 or dist[adj] > cost + d) and disappear[adj] > cost + d:
                    dist[adj] = cost + d
                    heappush(q, (dist[adj], adj))
        
        return dist