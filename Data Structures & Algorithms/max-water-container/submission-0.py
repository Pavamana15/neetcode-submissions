class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start , end = 0, len(heights)-1 
        out = []

        while start < end:
            volume = min(heights[start], heights[end])* (end - start)
            out.append(volume)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return max(out)


        