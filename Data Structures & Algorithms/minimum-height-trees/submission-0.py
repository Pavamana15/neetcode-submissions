class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i, edge in enumerate(edges):
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        print("Adjaceny matrix is :", adj)

        res = []
        visit = set()

        

        def dfs(root):
            result = 0
            if root in visit:
                return 0
            

            visit.add(root)

            for nei in adj[root]:
                if nei not in visit:
                    result = max(result, 1+dfs(nei))
                    
            return result

        for i in range(n):
            visit.clear()
            result = 0
            res.append([i,dfs(i)])

        print("The tree with different root and thier heightss are :", res)
        
        min_height = min(h for _, h in res)
        nodes = [node for node, h in res if h == min_height]

        return nodes




            
            


