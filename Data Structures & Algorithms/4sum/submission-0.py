class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()

        def Threesum(n, t):
            res = []
            for i, a in enumerate(n):
                if i > 0 and a == n[i-1]:
                    continue
                l,r = i+1, len(n)-1

                while l < r:
                   threesum = a + n[l] + n[r]

                   if threesum > t:

                    r -= 1 
                   elif threesum < t:

                    l += 1
                   else:
                    res.append([a,n[l],n[r]])
                    l += 1
                    while l < len(n) and n[l] == n[l-1]:
                        l += 1
                    
            return res

        for i, num in enumerate(nums):
            temp = []
            if i > 0 and num == nums[i-1]:
                    continue

            temp = Threesum(nums[i+1:], target - num)

            for l in temp:
                l.append(num)
                if sum(l) == target:
                    output.append(l)


        return output
            




                
                

                    