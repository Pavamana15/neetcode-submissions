class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        
        nums.sort()
        

        # Iterate through the list
        for i in range(len(nums) - 2):
            # Skip duplicate values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer approach
            start, end = i + 1, len(nums) - 1

            while start < end:
                cur_sum = nums[i] + nums[start] + nums[end]
                if cur_sum == 0:
                    result.append([nums[i], nums[start], nums[end]])
                    
                    # Skip duplicate values
                    while start < end and nums[start] == nums[start + 1]:
                        start += 1
                    while start < end and nums[end] == nums[end - 1]:
                        end -= 1
                    
                    # Move pointers
                    start += 1
                    end -= 1

                elif cur_sum < 0:
                    start += 1
                else:
                    end -= 1


        return result


        
