class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        num_true = hasApple.count(True)

        if num_true == 0:
            return 0

        adjcent = collections.defaultdict(list)
        for u, v in edges:
            adjcent[u].append(v)
            adjcent[v].append(u)

        
       
        def dfs(node,parent):

            

            time = 0
            
            
            for nei in adjcent[node]:
                if nei == parent:
                    continue
                child_time = dfs(nei,node)
                if child_time or hasApple[nei]:
                    time += 2 + child_time

                
                
                
            
            return time


        return dfs(0,-1)