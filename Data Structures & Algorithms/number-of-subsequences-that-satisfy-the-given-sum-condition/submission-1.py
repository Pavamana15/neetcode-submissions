class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        output = 0
        nums.sort()

        for i in range(len(nums)):
            cur_min = nums[i]

            if 2 * cur_min > target:
                break

            left, right = i, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if cur_min + nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            output += 2**(left-i-1)

            
            # for j in range(i, len(nums)):
                
            #     if cur_min + nums[j] <= target:
            #         if j == i:
            #             output += 1
            #         else:
            #             output += 2**(j-i-1)
            #     else:
            #         break
                

        return output % (10**9 + 7)