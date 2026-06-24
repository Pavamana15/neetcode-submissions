class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        cache = {}
        
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            if r == m:
                return 0

            score = points[r][c]

            max_score = 0

            for j in range(n):
                max_score = max(max_score, dfs(r+1,j)-abs(j-c))

            score += max_score

            cache[(r,c)] = score

            return cache[(r,c)]


        marks = 0

        for j in range(n):
            marks = max(marks,dfs(0,j))

        return marks        