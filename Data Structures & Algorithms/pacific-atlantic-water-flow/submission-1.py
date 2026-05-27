class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 1:
            return [[0,0]]
        
        rows, cols = len(heights), len(heights[0])
        visit = set()
        pacific = [ ] 
        atlantic = []

        
        for i in range(len(heights[0])):  
            pacific.append([0, i])         
        for j in range(len(heights)):      
            pacific.append([j, 0])  

        for i in range(len(heights[0])):  
            atlantic.append([len(heights)-1, i])         
        for j in range(len(heights)):      
            atlantic.append([j, len(heights[0])-1])        
 

        

        #ocean = pacific + atlantic
        print("The pacific :", pacific)
        print(" The atlantic :", atlantic)

        def bfs(r,c ):
            visit.clear()
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            print("The visit set are:", visit)
            ocean = []

            while q:
                
                
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if( r in range(rows) and
                        c in range(cols) and
                        heights[r][c] <= heights[row][col] and
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
                        
                        if [r, c] in pacific or [r, c] in atlantic:


                            ocean.append([r,c])

                        
                            ocean_set = set(map(tuple, ocean))
                            pacific_set = set(map(tuple, pacific))
                            atlantic_set = set(map(tuple, atlantic))

                        
                            has_pacific = bool(ocean_set & pacific_set)
                            has_atlantic = bool(ocean_set & atlantic_set)

                            if has_pacific and has_atlantic:
                                print("Ocean contains at least one element from both Pacific and Atlantic.")
                                return 1


            return -1

        Output = [[0] * len(heights[0]) for _ in range(len(heights))]

        for r in range(rows):
            for c in range(cols):
                if [r, c] in pacific and [r, c] in atlantic:
                    Output[r][c] = 1
                else:
                    Output[r][c] = bfs(r,c)

        print("The output is:", Output)

        indices_of_ones = [(i, j) for i in range(len(Output)) for j in range(len(Output[0])) if Output[i][j] == 1]

        return   indices_of_ones    
                
                        

