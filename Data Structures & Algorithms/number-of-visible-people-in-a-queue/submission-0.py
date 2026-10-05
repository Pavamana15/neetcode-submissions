class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights)
        stack = []

        for i in range(len(heights)-1,-1,-1):
            
            if not stack:
                stack.append(heights[i])

            else:
                while stack and heights[i] > stack[-1]:
                    answer[i] += 1
                    stack.pop()
                if stack:
                    answer[i] += 1
                stack.append(heights[i])
        return answer