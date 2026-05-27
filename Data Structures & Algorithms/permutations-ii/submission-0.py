class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        counts = Counter(nums)
        subset_count = Counter()

        def dfs():
            if len(subset)== len(nums):
                res.append(subset.copy())
                return

            for num in counts:
                subset_count[num] += 1

                if subset_count[num] > counts[num]:
                    subset_count[num] -= 1
                    continue
                else:

                    
                    
                    subset.append(num)
                    dfs()
                    subset.pop()
                    subset_count[num] -= 1

            

            

                

                

        dfs()
        return res