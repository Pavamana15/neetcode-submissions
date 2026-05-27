class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = []
        for num in nums:
            if num in hashmap:
                return num
            else:
                hashmap.append(num)
            


        