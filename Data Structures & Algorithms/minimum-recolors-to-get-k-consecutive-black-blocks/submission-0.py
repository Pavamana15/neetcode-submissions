class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left,recolor = 0,0
        output = float('inf')

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                recolor += 1
            
            # while right - left + 1 > k:
            #     if blocks[left] == 'W':
            #         recolor -= 1
            #     left += 1
            
            if right - left + 1 == k:
                output = min(output, recolor)
                if blocks[left] == 'W':
                    recolor -= 1
                left += 1
                

        return output