class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        return max(d, key=d.get)

        
