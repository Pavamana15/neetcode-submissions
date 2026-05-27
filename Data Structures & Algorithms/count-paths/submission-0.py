class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        output = [[0]*n for _ in range(m)]
        
        neighbour = {i: {j: [] for j in range(n)} for i in range(m)}
        for j in range(n):
            for i in range(m):
                if i+1 in range(m):
                    neighbour[i][j].append([i+1,j])
                if j+1 in range(n):
                    neighbour[i][j].append([i,j+1])
        
        visit = set()
        path = 0
        
        for row in neighbour:
            for col in neighbour[row]:
                print(f"Cell ({row}, {col}) neighbors: {neighbour[row][col]}")
                
        def dfs(k,l):
            nonlocal path
            if k == m-1 and l == n-1:
                path += 1
                return

            for x,y in neighbour[k][l]:
                dfs(x,y)


        dfs(0,0)

        return path



        