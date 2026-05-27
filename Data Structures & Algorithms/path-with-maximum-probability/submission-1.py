class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        Adj = collections.defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            Adj[u].append((v, p))
            Adj[v].append((u, p))


        minHeap = [(-1, start_node)]
        visit = set()
        p_success = -1
        
        while minHeap:
            p1, n1 = heapq.heappop(minHeap)

            if n1 == end_node:
                return -p1
            if n1 in visit:
                continue
            visit.add(n1)
            

            for n2, p2 in Adj[n1]:
                if n2 not in visit:
                    
                    heapq.heappush(minHeap, (p1*p2, n2))
        return 0