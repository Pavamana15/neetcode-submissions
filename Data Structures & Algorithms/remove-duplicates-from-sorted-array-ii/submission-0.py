class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        right = 0
        count = 0
        output = 0

        while right < len(nums):
            if right == 0:
                prev = nums[0]
                count += 1
                output += 1
                
            
            elif nums[right] == prev and count == 1:
                count += 1
                output += 1
                

            elif nums[right] == prev and count == 2:
                nums[right] = "_"
                
                
                
            elif nums[right] != prev:
                prev = nums[right]
                count = 1
                output += 1
                
            right += 1

        # print(f"The nums after removing duplicates : {nums}")

        right = len(nums) - 1

        for left in range(len(nums)-1,-1,-1):
            # print(f"The current nums : {nums}")
            # print(f"The value at {left} is {nums[left]}")
            if left == len(nums) - 1 and nums[left] == "_":
                continue
            elif left == len(nums) - 1 and nums[left] != "_":
                right = left

            elif left < len(nums) - 1 and nums[left] == "_":
                # print(f"Shifting ->>>>>>>>")
                i = left 
                while i < right:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    i += 1

                # right = left

        return output