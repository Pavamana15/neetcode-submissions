# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         ROWS, COLS = len(matrix), len(matrix[0])
#         visit = set()

#         def is_peak( i, j):
#             rows = len(matrix)
#             cols = len(matrix[0])
#             val = matrix[i][j]

            
#             if i > 0 and matrix[i - 1][j] > val:
#                 return False
            
#             if i < rows - 1 and matrix[i + 1][j] > val:
#                 return False
            
#             if j > 0 and matrix[i][j - 1] > val:
#                 return False
            
#             if j < cols - 1 and matrix[i][j + 1] > val:
#                 return False

#             return True

        

#         def dfs(r, c):
            
#             if (r < 0 or r >= ROWS or c < 0 or c >= COLS or is_peak(r,c) or
#                 (r, c) in visit):
#                 # if visit:
#                 #    visit.remove((r, c)) 
#                 return 0
            
#             visit.add((r, c))
#             #print("The visit sets is :", visit)

#             best = 0
            

#             best = max(dfs(r+1,c),dfs(r,c+1),dfs(r-1,c),dfs(r,c-1) )

#             visit.remove((r, c))  
#             return 1 + best

#         area = 0
#         for r in range(ROWS):
#             for c in range(COLS):
#                 print(f"Start DFS at ({r}, {c})")
#                 area = max(area, dfs(r, c))
#                 print(f"Max path length so far: {area}")
#         return area


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or matrix[r][c] <= prevVal
            ):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())