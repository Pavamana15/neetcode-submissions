class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        # for pos, spe in zip(position,speed):
        #     if (target-pos)/spe in stack:
        #         continue
        #     else:
        #         stack.append((target-pos)/spe)
        
        for pos, spe in sorted(zip(position,speed),reverse = True):
            
                
            if not stack or (target - pos)/spe > stack[-1]:
                stack.append((target-pos)/spe)
            

        
        return len(stack)
            



        