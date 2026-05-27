class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # visit = set()
        # visit.add((0,0))
        # t = 0
        # i = j = 0
        # output = []
        # output.append(grid[row-1][col-1])
        # output.append(grid[0][0])

        # while not (i == row-1 and j == col-1):

        #     min_val = float('inf')
        #     min_neighbors = []     
            # for dr, dc in directions:
            #     nr, nc = i + dr, j + dc

        #         if (nr,nc) == (row-1, col-1):
        #             return max(output)

                
                # if (nr, nc) in visit or nr < 0 or nc < 0 or nr >= row or nc >= col:

                #     continue

        #         val = grid[nr][nc]

        #         if val < min_val:
        #             min_val = val
        #             min_neighbors = [(nr, nc)]   
        #         elif val == min_val:
        #             min_neighbors.append((nr, nc)) 

        #     #print("The minimun neighbors are:", min_neighbors)
        #     if min_neighbors:
        #         i ,j=   min_neighbors[0]

        #     visit.add((i, j))

        #     print("The visit set is:", visit)


        #     output.append(grid[i][j])
        
        

        # return max(output)

        minHeap = [(grid[0][0],[0,0])]
        visit = set()
        t = 0

        output = []
        

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while minHeap:

            

            

            print("The min heap is :", minHeap)
            v1, (i, j) = heapq.heappop(minHeap)

            
            
            


            if (i,j) in visit:
                continue

            visit.add((i,j))

            print("The visit set is :", visit)

            t = max(t,v1)

            output.append(grid[i][j])

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (nr, nc) in visit or nr < 0 or nc < 0 or nr >= row or nc >= col:

                    continue

                heapq.heappush(minHeap, (max(v1 ,grid[nr][nc]), [nr,nc]))

            if i == row -1 and j == col -1:
                break
        
        print("The swimming path is :", output)
        return max(output)

        




            



        