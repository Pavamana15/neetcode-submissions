class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        cache = {}
        total = sum(nums)
        n = len(nums)
        def dfs(A,length,i):
            if (A,length,i) in cache:
                return cache[(A,length,i)]
            if i == len(nums):
                if length == 0 or length == n :
                    return False

                return A * n == total * length

            remaining = n - i
            possible = False
            for k in range(length, remaining +length):
                if (total * k) % n == 0:
                    possible = True
                    break
                    
            if possible:
                cache[(A,length,i)] = dfs(A+nums[i],length +1, i+1) or dfs(A,length, i+1)
                return cache[(A,length,i)]
            else:
                cache[(A,length,i)] = False
                return False

        return dfs(0,0,0)


            


            

        