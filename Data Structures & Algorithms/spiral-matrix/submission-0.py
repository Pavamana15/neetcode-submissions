# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

#         output = []

#         total_output = len(matrix) * len(matrix[0])

#         bottom = len(matrix) - 1
#         top = 0
#         left = 0
#         right = len(matrix[0]) - 1
#         i = 0
#         j = 0

#         while len(output) != total_output:
            
#             if top != bottom and left != right and i <= right:
#                 output.append(matrix[top][i])
#                 i += 1

#             elif i == right and j <= bottom :
#                 output.append(matrix[j][right])
#                 j += 1

#             elif j == bottom and i >= left:
#                 output.append(matrix[bottom][i])
#                 i -= 1

#             elif i == left and j >= top:
#                 output.append(matrix[j][left])
#                 j -= 1

            
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

            



        



        

        

        
        

            


        