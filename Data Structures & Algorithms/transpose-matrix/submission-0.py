class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        output = []

        for i in range(n):
            cur = []
            for j in range(m):
                cur.append(matrix[j][i])

            output.append(cur)
                
        return output
