class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [ [] ]

        if not nums:
            return res

        for num in nums:
            for existing_subset in res[:]:  
                print("The existing subset is:",existing_subset )
                new_subset = existing_subset + [num]
                res.append(new_subset)
                print("The new subset is :", new_subset)
                print("The current subset is:", res)  

        return res         
        