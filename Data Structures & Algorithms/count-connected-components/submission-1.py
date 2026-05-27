class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # if not n:
        #     return False
        
        # adj = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        
        # visit = set()
        # def dfs(node, par):
        #     if node in visit:
        #         return len(visit)
            
        #     visit.add(node)
        #     for nei in adj[node]:
        #         if nei == par:
        #             continue
        #         dfs(nei, node)
        
        
        # connected_components = 0
        # i = 0
        # print("The visit set is:", visit)

        # # Loop through each node in the graph
        # for i in range(n):
        #     # If node `i` is not in `visit`, it's a new connected component
        #     if i not in visit:
        #         # Run DFS from node `i` to mark all reachable nodes in this component
        #         if dfs(i, -1) < n:  # Assuming `dfs` returns `True` when it completes a component
        #             connected_components += 1
        #             print("Connected component found. Total components so far:", connected_components)
                
        # print("Length of visit is:", len(visit))

        # print("Total connected components:", connected_components)
        # return connected_components

        if not n:
            return 1

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        print("The adjacency matrix is:", adj)
        
        visit = set()

        def bfs(node, par):
            visit.clear()
            q = collections.deque()
            visit.add(node)
            q.append(node)

            print("The visit set are:", visit)

            while q:
                current_node = q.popleft()
                for neigh in adj[current_node]:
                    if neigh != par and neigh not in visit:
                        q.append(neigh)
                        visit.add(neigh)

        
        connected_components = {i: [0] for i in range(n)}
        count = 1
        
        for key, value in connected_components.items():
            if value == [0]:

                print("Key is :", key)  
                bfs(key,-1)
                print("The visit set is:", visit)
                for i in visit:
                    connected_components[i] = count
                count += 1
        print("The connected components are:",connected_components)
        return max(connected_components.values())
        
