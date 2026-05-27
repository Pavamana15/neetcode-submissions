class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        Adj = {i: [] for i in range(len(isConnected))}

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    Adj[i].append(j)

        visit = set()
        provinces = 0

        def dfs(c):

            if c in visit:
                return
            
            visit.add(c)

            for neigh in Adj[c]:
                dfs(neigh)


        for i in range(len(isConnected)):
            if i not in visit:
                dfs(i)
                provinces += 1

        return provinces
        


            
                