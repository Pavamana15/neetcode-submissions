class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(graph, start, n):
            dist = {i: float('inf') for i in range(1, n+1)}
            dist[start] = 0
            visited = set()

            while len(visited) < n:
                # Pick the unvisited node with smallest distance
                u = None
                for node in range(1, n+1):
                    if node not in visited:
                        if u is None or dist[node] < dist[u]:
                            u = node

                if u is None:
                    break

                visited.add(u)

                # Update distances
                for v, w in graph.get(u, []):
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

            return dist


        # Input conversion
        

        graph = {}
        for u, v, w in times:
            graph.setdefault(u, []).append((v, w))

        distances = dijkstra(graph, k, n)
        return -1 if float('inf') in distances.values() else max(distances.values())



        
        