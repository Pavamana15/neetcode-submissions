class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix[0])):
                        if isinstance(matrix[i][k], (int, float)) and matrix[i][k] != 0:
                            matrix[i][k] = 'Z'
                    for k in range(len(matrix)):
                        if isinstance(matrix[k][j], (int, float)) and matrix[k][j] != 0:
                            matrix[k][j] = 'Z'
        print("The pre final matrixx is :", matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'Z':
                    matrix[i][j] = 0

        print("The final matrixx is :", matrix)

        
        
        
        