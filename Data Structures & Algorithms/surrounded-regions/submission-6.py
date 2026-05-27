class Solution:
    def solve(self, board: List[List[str]]) -> None:

        rows, cols = len(board), len(board[0])
        visit = set()
        
        res = []

        def bfs(r,c ):
            visit.clear()
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            print("The visit set are:", visit)

            while q:
                print("Search Started")
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if( r in range(rows) and
                        c in range(cols) and
                        board[r][c] == 'O' and
                        
                        (r,c) not in visit):
                        q.append((r,c))
                        visit.add((r,c))
            
            # print("The length of visit is:", len(visit))
            # return len(visit) == 4

                        
            
            
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == 'O':
                    print("The current (r,c) is:", r, c)
                    bfs(r, c)  
                    print("The visit set is:", visit)

                    
                    # Initialize the flag for all conditions being met
                    all_conditions_met = True

                    # Loop through each (row, col) in visit
                    for row, col in visit:
                        # Loop through each direction (dr, dc)
                        for dr, dc in directions:
                            # Calculate the neighboring cell position
                            nr, nc = row + dr, col + dc
                            
                            # Check if the neighboring cell is within bounds
                            if not (0 <= nr < rows and 0 <= nc < cols):
                                all_conditions_met = False
                                break
                            
                            # Check if the neighboring cell contains 'X'
                            if board[nr][nc] != 'X' and (nr, nc) not in visit:
                                all_conditions_met = False
                                break
                            
                            

                        # If any of the conditions are not met, no need to check further
                        if not all_conditions_met:
                            break

                    # If conditions are met, convert all visited positions to 'X'
                    if all_conditions_met:
                        for indices in visit:
                            row, col = indices
                            board[row][col] = 'X'

                #    if bfs(r, c):
                #       if board[r-1][c] == 'X' and board[r-1][c+1] == 'X' and board[r][c-1] == 'X' and board[r+1][c-1] == 'X' and board[r+2][c] == 'X' and board[r+2][c+1] == 'X' and board[r][c+2] == 'X' and board[r+1][c+2] == 'X':
                #          for indices in visit:
                #             row, col = indices
                #             board[row][col] = 'X'

        
                        
                        
                       

                      
                   