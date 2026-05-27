class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        n = len(matrix)

        
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print("The transposed matrix is:", matrix)

        print("The number of rows are:", rows)
        print("The number of columns are:", cols)

        for i in range(rows):
            print("The current row is:",i)

            start = 0
            end = cols-1

            while start < end :
                temp = matrix[i][start]
                matrix[i][start] = matrix[i][end]
                matrix[i][end] = temp

                start += 1
                end -= 1

        print("The final rotated image is:", matrix)
        
        